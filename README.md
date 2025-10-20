# HTL Film-Suchbrowser

## Beschreibung
Der **HTL Film-Suchbrowser** ist eine kleine Web-App, mit der man Filme nach Titel suchen kann.  
Die App zeigt eine Liste von gefundenen Filmen an, inklusive:

- Poster
- Titel
- Jahr
- Regisseur
- Genre
- IMDb Bewertung
- Plot (Handlung)

Die Daten kommen von der **OMDb API** (Open Movie Database).

---

## Funktionsweise
1. Du gibst einen Filmtitel in die Suchleiste ein.
2. Die App sucht über die OMDb API nach Filmen, die zum Titel passen.
3. Gefundene Filme werden in ausklappbaren Bereichen (Expanders) angezeigt.
4. Wenn man auf einen Film klickt, sieht man alle Details und das Poster (falls verfügbar).

---

## Benötigte Software
- Python 3.x
- Streamlit
- Requests-Bibliothek

---

## Installation

1. Repository klonen oder Dateien herunterladen.
2. In der Kommandozeile ins Projektverzeichnis wechseln.
3. Virtuelle Umgebung erstellen (optional, empfohlen):
   ```bash
   python -m venv venv
   source venv/bin/activate  # für Linux/Mac
   venv\Scripts\activate     # für Windows
