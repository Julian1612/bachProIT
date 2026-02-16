# 🎓 Bachelor Professional IT - Lernkarten Sammlung

> [!IMPORTANT]
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

### 1. Anki Design (Template) einrichten
Damit das Layout funktioniert, muss der Notiztyp exakt so konfiguriert sein:

1.  **Notiztyp erstellen:** Gehe in Anki auf **Werkzeuge** -> **Notiztypen verwalten** -> **Hinzufügen**. Wähle "Einfach" und nenne ihn **`BachelorProIT`**.
2.  **Felder zwingend anpassen:** Markiere den neuen Typ `BachelorProIT` und klicke rechts auf **Felder...**. 
    * Benenne die Felder exakt so um (oder füge sie hinzu):
        1. **`Vorderseite`**
        2. **`Rückseite`**
    * *Hinweis: Ohne diese exakten Namen findet das Template die Daten nicht!*
3.  **Code einfügen:** Klicke in der Notiztypen-Verwaltung auf **Karten...** und kopiere den Code aus dem Repo:
    * Inhalt von `front.html` -> **Vorderseite**
    * Inhalt von `back.html` -> **Rückseite**
    * Inhalt von `style.css` -> **Formatierung**

### 2. Karten importieren
1. Wähle in Anki **Datei** -> **Importieren**.
2. Wähle eine CSV-Datei aus dem Repo.
3. **Wichtig:** * Trennzeichen: Pipe-Symbol (**`|`**).
    * Notiztyp: **`BachelorProIT`**.
    * Stelle sicher, dass die CSV-Spalten den Feldern "Vorderseite" und "Rückseite" korrekt zugeordnet sind.

---

## 🚀 Der Workflow: Klasse statt Masse

Wir fokussieren uns auf einzelne, relevante Themen statt auf riesige Textwüsten.

1. **Themenwahl:** Pick dir ein wichtiges Thema aus dem Skript heraus.
2. **Zusammenfassen (NotebookLM):** Nutze den Prompt aus `Promts/NootbookLMPromt.md`.
3. **Karten erstellen (Gemini):** Nutze den Prompt aus `Promts/GoogleGemPromt.md`.
4. **Qualitätskontrolle:** Lies die Karten kritisch durch. Korrigiere Fehler oder ergänze Fehlendes sofort. Multiple-Choice-Karten können weggelassen werden, wenn sie keinen Mehrwert bieten.

### 🔍 Regeln zur Qualitätssicherung (Handlungsanweisung)

Damit das Repository für alle nützlich bleibt, halte dich beim Erstellen und Prüfen an diese goldenen Regeln:

* **Faktencheck-Pflicht:** Gleiche KI-generierte Definitionen immer mit den Skripten oder anderen Lehrmaterialien ab. Fachbegriffe müssen korrekt verwendet werden.
* **Das Prinzip der Atomarität:** Eine Karte = Eine Information. Erstelle keine "Monster-Karten" mit 10 Aufzählungspunkten. Wenn eine Antwort zu lang ist, teile sie in mehrere kleine Karten auf. 
* **Kontext wahren:** Achte darauf, dass die Frage eindeutig ist. Man sollte schon an der Frage erkennen, aus welchem Lernbereich  das Thema stammt.
* **Verständnis vor Auswendiglernen:** Wenn die KI eine Antwort zu kompliziert formuliert, schreibe sie in deinen eigenen Worten um. Du musst die Logik dahinter verstehen, nicht nur den Text reproduzieren.
* **Kein Datenmüll:** * Lösche redundante Karten (doppelte Inhalte).
    * Karten, die nur "Ja/Nein" Antworten erfordern, sind meist wertlos – wandle sie in "Erkläre..." oder "Nenne die 3 Merkmale von..." um.
* **Format-Check:** Prüfe vor dem Commit, ob das Pipe-Symbol (`|`) korrekt als Trenner sitzt und keine Zeilenumbrüche innerhalb der Felder den Import zerschießen.

---

## 🤝 Mitmachen & Beitragen

Dieses Repo lebt davon, dass alle mit anpacken. Wenn wir unsere Ressourcen teilen, haben wir alle eine bessere Vorbereitung und mehr Zeit.

* **Committen:** Du hast ein Thema gut aufbereitet? Lade die CSV hier hoch!
* **Korrigieren:** Fehler gefunden? Fix ihn und mach einen Commit.
* **Optimieren:** Du hast bessere Prompts oder ein schöneres Design? Her damit!

Lasst uns gemeinsam das Studium effizienter gestalten. Viel Erfolg!