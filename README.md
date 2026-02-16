🎓 Bachelor Professional IT - Lernmaterial & AI-Workflow
========================================================

Dieses Repository ist eine zentrale Anlaufstelle für Studierende zum **Bachelor Professional IT (IHK)**. Ziel ist es, die Prüfungsvorbereitung effizienter zu gestalten, indem wir hochwertiges Lernmaterial teilen und moderne KI-Tools nutzen, um komplexe Themen verständlich aufzubereiten.

Hier geht es nicht darum, ganze Skripte stumpf zu kopieren, sondern gezielt die Themen herauszufiltern, die wirklich prüfungsrelevant und lernenswert sind -- **Klasse statt Masse**.

📂 Struktur des Repositories
----------------------------

-   **`ITM/` & `OuP/`**: Themenspezifische Karteikarten (CSV-Format) für Bereiche wie IT-Management sowie Organisation und Personalentwicklung.

-   **`flashCardsTemp/`**: Enthält das Design für deine Anki-Karten (`front.html`, `back.html` und `style.css`), damit die Karten auf allen Geräten übersichtlich und professionell aussehen.

-   **`Promts/`**:

    -   `NootbookLMPromt.md`: Optimiert für Google NotebookLM, um aus langen Skripten prägnante Zusammenfassungen einzelner Themen zu erstellen.

    -   `GoogleGemPromt.md`: Ein spezieller Prompt für Google Gemini, um aus diesen Zusammenfassungen hochwertige, logisch strukturierte Karteikarten zu generieren.

* * * * *

⚙️ Einrichtung & Konfiguration
------------------------------

### 1\. Anki Design anlegen

Damit die Karten korrekt angezeigt werden, musst du einmalig den Notiztyp in Anki anpassen:

1.  Öffne Anki: `Werkzeuge` -> `Notiztypen verwalten` -> `Hinzufügen`.

2.  Wähle "Einfach" als Vorlage und nenne ihn `BachelorProIT`.

3.  Klicke auf `Karten...` und kopiere die Inhalte aus dem Ordner `flashCardsTemp/`:

    -   Inhalt von `front.html` in das Feld **Vorderseite**.

    -   Inhalt von `back.html` in das Feld **Rückseite**.

    -   Inhalt von `style.css` in das Feld **Formatierung**.

### 2\. Karten importieren

1.  Wähle in der Anki-Hauptansicht `Datei` -> `Importieren`.

2.  Wähle eine CSV-Datei (z.B. aus `ITM/`).

3.  Stelle sicher, dass als Trennzeichen das Pipe-Symbol (`|`) ausgewählt ist und der Notiztyp auf `BachelorProIT` steht.

* * * * *

🚀 Workflow: Gezielte Erstellung hochwertiger Karten
----------------------------------------------------

Der Fokus liegt auf der Erarbeitung einzelner, komplexer Themenbereiche. Wir wollen keine "Daten-Müllhalde", sondern Karten, die das Verständnis fördern.

1.  **Thema auswählen:** Identifiziere ein spezifisches Thema im IHK-Skript, das du vertiefen möchtest.

2.  **Zusammenfassung (NotebookLM):** Nutze den Prompt aus `Promts/NootbookLMPromt.md`, um das Thema kompakt auf den Punkt zu bringen.

3.  **Karten generieren (Gemini):** Kopiere die Zusammenfassung in Google Gemini zusammen mit dem Prompt aus `Promts/GoogleGemPromt.md`. Die KI erstellt dir daraus präzise Karteikarten, die genau die Kernpunkte treffen.

4.  **Qualitätscheck:** Lies die generierten Karten kurz durch. Nur was wirklich sinnvoll ist, wandert in dein Anki-Deck.

* * * * *

🤝 Mitmachen & Beitragen
------------------------

Dieses Studium ist fordernd genug -- wenn wir unsere Ressourcen bündeln, sparen wir alle Zeit und Energie.

-   **Committen:** Wenn du für ein Thema gute Karten erstellt hast, füge sie dem Repo hinzu.

-   **Verbessern:** Findest du Fehler in bestehenden CSVs oder hast einen besseren Prompt? Erstelle einen Pull-Request.

-   **Teilen:** Je mehr Leute mitmachen, desto lückenloser wird unsere Vorbereitung.

Lasst uns gemeinsam dafür sorgen, dass wir mit top Lernmaterial in die Prüfungen gehen!

* * * * *