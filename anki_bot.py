import sys
import os
import subprocess
import csv
import time
import json

# --- KONFIGURATION ---
ANKI_URL = "http://localhost:8765"
ANKI_MODEL = "AnkiPro"  # Dein neuer Notiztyp
DEFAULT_KURS = "Bachelor Professional IT"

# Mapping der CSV-Spalten zu den Anki-Feldern (Reihenfolge muss in CSV stimmen!)
FIELD_NAMES = [
    "Kurs",             # Index 0
    "Thema",            # Index 1
    "Frage",            # Index 2
    "Hinweis_1",        # Index 3
    "Hinweis_2",        # Index 4
    "Antwort",          # Index 5
    "Extra",            # Index 6
    "Real_World_Case",  # Index 7
    "Mnemonik",         # Index 8
    "Tags"              # Index 9 (Wird auch als echtes Anki-Tag gesetzt)
]

# Deine Dateitypen
STACKS = {
    "itm": {"file": "itm.csv", "deck": "ITM"},
    "oup": {"file": "oup.csv", "deck": "OUP"}
}

# --- 1. FAIL-SAFE: BIBLIOTHEKEN ---
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"⚠️  Modul '{package}' fehlt.")
        if input(f"Installieren? (j/n): ").lower() == 'j':
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            sys.exit(1)

install_and_import('requests')
import requests

# --- 2. ANKI CONNECTION ---
def check_anki():
    try:
        requests.get(ANKI_URL)
        return True
    except requests.exceptions.ConnectionError:
        print("⚠️  Anki ist nicht offen.")
        input("👉 Bitte Anki öffnen und [ENTER] drücken...")
        try:
            requests.get(ANKI_URL)
            return True
        except:
            return False

# --- 3. GIT SYNC ---
def sync_git(filename):
    print(f"\n--- 1. Git Sync für {filename} ---")
    if not os.path.exists(filename):
        print(f"❌ Datei {filename} fehlt!")
        return False
    
    try:
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)
        
        subprocess.run(["git", "add", filename], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        
        if filename in status.stdout:
            msg = f"Update {filename} ({time.strftime('%Y-%m-%d %H:%M')})"
            subprocess.run(["git", "commit", "-m", msg], check=True)
            print("✅ Git Commit erstellt.")
            try:
                subprocess.run(["git", "push"], check=True)
                print("✅ Push erfolgreich.")
            except:
                print("⚠️  Push nicht möglich (kein Remote?), aber lokal gesichert.")
        else:
            print("ℹ️  Keine Änderungen für Git.")
        return True
    except Exception as e:
        print(f"❌ Git Fehler: {e}")
        return False

# --- 4. ANKI IMPORT ---
def sync_anki(filename, deckname):
    print(f"\n--- 2. Anki Import ({ANKI_MODEL}) ---")
    new_notes = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Versuche Semikolon (Excel Standard DE) oder Komma zu erkennen
            try:
                dialect = csv.Sniffer().sniff(f.read(2048), delimiters=";,")
            except:
                dialect = 'excel' # Fallback
            
            f.seek(0)
            reader = csv.reader(f, dialect)
            
            for row_idx, row in enumerate(reader):
                # Leere Zeilen überspringen
                if not row: continue
                
                # Sicherstellen, dass die Zeile genug Spalten hat (auffüllen mit Leerstring)
                while len(row) < len(FIELD_NAMES):
                    row.append("")

                # Daten zuordnen
                fields = {}
                tags_list = []

                # Spezialbehandlung: Tags (letzte Spalte)
                raw_tags = row[9]
                if raw_tags:
                    # Trennt bei Leerzeichen (z.B. "IT-Security ISO27001")
                    tags_list = raw_tags.split(" ")
                
                # Spezialbehandlung: Kurs (Standardwert setzen, falls leer)
                if not row[0].strip():
                    row[0] = DEFAULT_KURS

                # Felder befüllen
                for i, field_name in enumerate(FIELD_NAMES):
                    # Zeilenumbrüche für HTML konvertieren (optional, falls du im CSV "Enter" drückst)
                    content = row[i].replace("\n", "<br>")
                    fields[field_name] = content

                note = {
                    "deckName": deckname,
                    "modelName": ANKI_MODEL,
                    "fields": fields,
                    "tags": tags_list,
                    "options": {
                        "allowDuplicate": False,
                        "duplicateScope": "deck"
                    }
                }
                new_notes.append(note)

        if new_notes:
            payload = {"action": "addNotes", "version": 6, "params": {"notes": new_notes}}
            response = requests.post(ANKI_URL, json=payload).json()
            
            if response.get("error"):
                print(f"❌ Anki Fehler: {response['error']}")
            else:
                # Zähle echte Imports (nicht None)
                imported = len([x for x in response['result'] if x is not None])
                print(f"✅ {imported} Karte(n) importiert.")
                if imported < len(new_notes):
                    print(f"ℹ️  {len(new_notes) - imported} Duplikate ignoriert.")
        else:
            print("ℹ️  CSV war leer.")

    except Exception as e:
        print(f"❌ Import Fehler: {e}")

# --- MAIN ---
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in STACKS:
        print("Nutzung: push-itm oder push-oup")
        sys.exit(1)

    target = sys.argv[1]
    cfg = STACKS[target]

    if check_anki():
        if sync_git(cfg["file"]):
            sync_anki(cfg["file"], cfg["deck"])