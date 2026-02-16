🎓 Bachelor Professional IT - Lernkarten Sammlung
=================================================

> [!CAUTION]
>
> ### 🛑 WICHTIGER HINWEIS ZUR KI-NUTZUNG
>
> **KI ist ein Hilfsmittel, kein Ersatz für das Gehirn!** > Wir nutzen hier KI, um den Lernprozess zu beschleunigen. Das ist legitim und sinnvoll, aber: **KI halluziniert und macht Fehler.** > * **Kopiere niemals blind generierte Karten.** > * **Prüfe jeden Inhalt ausführlich** auf Richtigkeit und Vollständigkeit, bevor du ihn lernst.
>
> -   Nutze KI nicht als einziges Werkzeug -- erstelle auch eigene Karten manuell, um den Stoff wirklich zu verstehen.
>
>
> -   **Qualität und fachliche Richtigkeit stehen an oberster Stelle!**

* * * * *

Diese Sammlung dient dazu, Lernmaterialien für den **Bachelor Professional IT (IHK)** zentral zu sammeln. Anstatt dass jeder seine eigenen Zusammenfassungen und Karten mühsam von Null erstellt, teilen wir hier unsere Ergebnisse, um uns gegenseitig zu unterstützen und Zeit zu sparen.

Es geht hier nicht darum, Masse zu produzieren, sondern gezielt hochwertige Karten zu den Themen zu erstellen, die es wirklich wert sind, gelernt zu werden.

📂 Inhalt des Repositories
--------------------------

-   **`ITM/` & `OuP/`**: Sammlungen von Karteikarten (CSV-Format) für die Bereiche IT-Management sowie Organisation und Personal.

-   **`flashCardsTemp/`**: Das Design-Template für Anki, damit deine Karten professionell und einheitlich aussehen (`front.html`, `back.html`, `style.css`).

-   **`Promts/`**:

    -   `NootbookLMPromt.md`: Optimierter Prompt für Google NotebookLM, um gezielt Themen aus Skripten zusammenzufassen.

    -   `GoogleGemPromt.md`: Prompt für Google Gemini, um aus Zusammenfassungen fertige CSV-Listen für Anki zu machen.

* * * * *

⚙️ Einrichtung & Konfiguration
------------------------------

### 1\. Anki Design (Template)

Damit das Layout der Karten stimmt, musst du den Notiztyp in Anki einmalig anlegen:

1.  Gehe in Anki auf **Werkzeuge** -> **Notiztypen verwalten** -> **Hinzufügen**.

2.  Wähle "Einfach" und nenne ihn z.B. `BachelorProIT`.

3.  Klicke auf **Karten...** und kopiere die Inhalte aus dem Ordner `flashCardsTemp/` in die Felder:

    -   `front.html` -> **Vorderseite**

    -   `back.html` -> **Rückseite**

    -   `style.css` -> **Formatierung**

### 2\. Karten importieren

1.  Wähle in Anki **Datei** -> **Importieren**.

2.  Wähle eine CSV-Datei aus dem Repository.

3.  Stelle sicher, dass als Trennzeichen das Pipe-Symbol (`|`) eingestellt ist und der Notiztyp auf `BachelorProIT` steht.

* * * * *

🚀 Der Workflow: Klasse statt Masse
-----------------------------------

Wir fokussieren uns auf einzelne, relevante Themen statt auf riesige Textwüsten.

1.  **Gezielte Themenwahl:** Pick dir ein wichtiges Thema aus dem IHK-Skript heraus.

2.  **Zusammenfassen (NotebookLM):** Nutze den Prompt aus `Promts/NootbookLMPromt.md`, um eine prägnante Zusammenfassung zu erhalten.

3.  **Karten erstellen (Gemini):** Kopiere die Zusammenfassung zusammen mit dem Prompt aus `Promts/GoogleGemPromt.md` in Google Gemini.

4.  **Qualitätskontrolle:** Lies die Karten kritisch durch. Korrigiere Fehler oder ergänze Fehlendes sofort. Multiple-Choice-Karten können weggelassen werden, wenn sie keinen Mehrwert bieten.

* * * * *

🤝 Mitmachen & Beitragen
------------------------

Dieses Repo lebt davon, dass alle mit anpacken. Wenn wir unsere Ressourcen teilen, haben wir alle eine bessere Vorbereitung und mehr Zeit für die wichtigen Dinge.

-   **Committen:** Du hast ein Thema gut aufbereitet? Lade die CSV hier hoch!

-   **Korrigieren:** Du hast einen Fehler in einer Karte gefunden? Fix ihn und mach einen Commit.

-   **Optimieren:** Du hast einen besseren Prompt oder ein schöneres CSS? Her damit!

Lasst uns gemeinsam das Studium effizienter gestalten und uns gegenseitig zum Abschluss verhelfen. Viel Erfolg!