# 🎓 Bachelor Professional IT - Lernkarten Sammlung

> [!WARNING]
> # 🛑 ABSOLUTE PRIORITÄT: QUALITÄT & KI-CHECK
>
> **KI ist ein mächtiges Hilfsmittel, aber sie ist NICHT fehlerfrei! Nutze sie legitim zur Unterstützung, aber halte dich an diese Regeln:**
>
> * 🧠 **KI ERSETZT NICHT DEIN GEHIRN:** Die KI hilft beim Strukturieren, aber das echte Lernen und Verstehen musst du selbst übernehmen.
> * ⚠️ **KI HALLUZINIERT STARK:** KI-Modelle erfinden Fakten oder verdrehen Details. **VERTRAUE DER KI NIEMALS BLIND!**
> * 🚫 **KEIN BLINDES KOPIEREN:** Jede generierte Karte muss vor dem Import zwingend gelesen und kritisch hinterfragt werden.
> * ✅ **MANUELLE PRÜFUNG:** Kontrolliere jede Karte auf fachliche Richtigkeit und Vollständigkeit. Fehlt etwas Wichtiges?
> * ✍️ **MACHE EIGENE KARTEN:** Nutze KI nicht als einziges Werkzeug. Manuell erstellte Karten sind oft der beste Weg, um komplexe Themen wirklich zu durchdringen.
> * 🔝 **QUALITÄT VOR MASSE:** Die Richtigkeit der Inhalte steht an oberster Stelle. Unnötige Kleinigkeiten oder Multiple-Choice-Fragen ohne Mehrwert können (und sollten) weggelassen werden.

---

Diese Sammlung dient dazu, Lernmaterialien für den **Bachelor Professional IT (IHK)** zentral zu sammeln. Anstatt dass jeder seine eigenen Zusammenfassungen und Karten mühsam von Null erstellt, teilen wir hier unsere Ergebnisse, um uns gegenseitig zu unterstützen und Zeit zu sparen.

Es geht hier nicht um Masse, sondern um gezielte Qualität. Wir bereiten Themen auf, die wirklich prüfungsrelevant sind.

## 📂 Inhalt des Repositories

* **`ITM/` & `OuP/`**: Sammlungen von Karteikarten (CSV-Format) für die Bereiche IT-Management sowie Organisation und Personal.
* **`flashCardsTemp/`**: Das Design-Template für Anki (`front.html`, `back.html`, `style.css`).
* **`Promts/`**: 
    * `NootbookLMPromt.md`: Prompt für Google NotebookLM (Zusammenfassung einzelner Themen).
    * `GoogleGemPromt.md`: Prompt für Google Gemini (Erstellung der Anki-Karten aus Texten).

---

## ⚙️ Einrichtung & Konfiguration

### 1. Anki Design (Template)
Damit das Layout der Karten stimmt, musst du den Notiztyp in Anki einmalig anlegen:

1. Gehe in Anki auf **Werkzeuge** -> **Notiztypen verwalten** -> **Hinzufügen**.
2. Wähle "Einfach" und nenne ihn z.B. `BachelorProIT`.
3. Klicke auf **Karten...** und kopiere die Inhalte aus dem Ordner `flashCardsTemp/` in die Felder:
    * `front.html` -> **Vorderseite**
    * `back.html` -> **Rückseite**
    * `style.css` -> **Formatierung**

### 2. Karten importieren
1. Wähle in Anki **Datei** -> **Importieren**.
2. Wähle eine CSV-Datei aus dem Repository.
3. Stelle sicher, dass als Trennzeichen das Pipe-Symbol (`|`) eingestellt ist und der Notiztyp auf `BachelorProIT` steht.

---

## 🚀 Der Workflow: Klasse statt Masse

Wir fokussieren uns auf einzelne, relevante Themen statt auf riesige Textwüsten.

1. **Themenwahl:** Pick dir ein wichtiges Thema aus dem IHK-Skript heraus.
2. **Zusammenfassen (NotebookLM):** Nutze den Prompt aus `Promts/NootbookLMPromt.md`.
3. **Karten erstellen (Gemini):** Nutze den Prompt aus `Promts/GoogleGemPromt.md`.
4. **Qualitätskontrolle:** Lies die Karten kritisch durch. Korrigiere Fehler oder ergänze Fehlendes sofort. Multiple-Choice-Karten können weggelassen werden, wenn sie keinen Mehrwert bieten.

---

## 🤝 Mitmachen & Beitragen

Dieses Repo lebt davon, dass alle mit anpacken. Wenn wir unsere Ressourcen teilen, haben wir alle eine bessere Vorbereitung und mehr Zeit.

* **Committen:** Du hast ein Thema gut aufbereitet? Lade die CSV hier hoch!
* **Korrigieren:** Fehler gefunden? Fix ihn und mach einen Commit.
* **Optimieren:** Du hast bessere Prompts oder ein schöneres Design? Her damit!

Lasst uns gemeinsam das Studium effizienter gestalten. Viel Erfolg!