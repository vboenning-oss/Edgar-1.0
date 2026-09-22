# Edgar-1.0
Lokaler KI Chat, inspiriert vom Film Electric Dreams<img width="1408" height="881" alt="SCR-20260922-rque" src="https://github.com/user-attachments/assets/12db3107-3c83-4c40-a0e5-d8916ba8f8f6" />
<img width="1408" height="881" alt="SCR-20260922-rpdb" src="https://github.com/user-attachments/assets/2d19bbe0-fd58-4f99-ba5d-11440ffdbd0f" />

EDGAR 1.0

Ein kleiner, lokaler KI-Assistent für den Mac.

EDGAR ist ein lokaler KI-Assistent, der derzeit für macOS entwickelt wurde und auf einem kompatiblen Mac ausgeführt werden kann.

EDGAR entstand aus einem privaten Lern- und Bastelprojekt und wurde ursprünglich unter dem Namen MIMIR entwickelt.

Created by Volker — Started with no programming experience.

⸻

🚀 Funktionen

* Lokale Verarbeitung der Eingaben
* Keine zwingende Cloud-Anbindung
* Verschiedene Persönlichkeiten und Systemprompts
* Eigenen Systemprompt verwenden
* Lokales Gedächtnis für ausgewählte Funktionen
* Ausführbare Version für eine einfache Nutzung
* Sprachmodell wird bei Bedarf lokal bereitgestellt

⸻

🍎 Aktuelle Plattform

EDGAR 1.0 läuft derzeit ausschließlich auf macOS.

Die aktuelle Version wurde für den Mac entwickelt und getestet.

Eine Unterstützung für weitere Betriebssysteme, insbesondere Windows, ist für eine zukünftige Version grundsätzlich möglich, aber in EDGAR 1.0 noch nicht umgesetzt.

⸻

🧠 Sprachmodell

EDGAR enthält kein Sprachmodell in der Anwendung.

Beim Einrichten bzw. ersten Start kann das benötigte Sprachmodell separat heruntergeladen und lokal gespeichert werden.

Das hat mehrere Vorteile:

* Die Programmdatei bleibt relativ klein.
* Das Sprachmodell kann unabhängig von EDGAR aktualisiert oder ausgetauscht werden.
* Das Modell muss nicht bei jeder Installation erneut in die Anwendung integriert werden.

Wichtig

Das verwendete Sprachmodell ist nicht Bestandteil der EDGAR-Lizenz.

Für das Sprachmodell gelten ausschließlich die jeweiligen Lizenzbedingungen des Modellherstellers bzw. der jeweiligen Modellversion.

Bitte prüfe diese Lizenzbedingungen vor einer kommerziellen Nutzung oder Weitergabe.

⸻

📦 Installation

Die aktuelle EDGAR-Version ist für macOS vorgesehen.

Bei einer fertigen ausführbaren Version müssen grundsätzlich keine Python-Kenntnisse vorhanden sein.

Das Sprachmodell wird separat benötigt und kann mehrere Gigabyte Speicherplatz benötigen.

⸻

🛠️ Quellcode

EDGAR ist freie Software.

Der Quellcode darf:

* verwendet,
* untersucht,
* verändert,
* kopiert,
* weitergegeben und
* für eigene Projekte angepasst

werden.

Änderungen und eigene Versionen dürfen veröffentlicht werden.

Bitte beachte dabei die Lizenzbedingungen eventuell verwendeter Drittanbieter-Software und insbesondere des verwendeten Sprachmodells.

⸻

📜 Lizenz

EDGAR 1.0 wird unter der MIT License veröffentlicht.

Copyright (c) 2026 Volker Boenning

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, and to permit persons to whom the software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

⸻

⚠️ Hinweis zu Drittanbieter-Komponenten

EDGAR kann Software, Bibliotheken oder Sprachmodelle anderer Projekte verwenden.

Diese Komponenten bleiben Eigentum ihrer jeweiligen Urheber bzw. Rechteinhaber.

Für diese Komponenten gelten deren eigene Lizenzbedingungen.

Insbesondere gilt:

Die freie MIT-Lizenz von EDGAR überträgt keine Rechte an einem verwendeten Sprachmodell.

⸻

❤️ Hintergrund

EDGAR ist aus einem einfachen Experiment entstanden:

Ein eigenes kleines KI-System bauen, verstehen, ausprobieren und immer weiter verbessern.

Das Projekt begann ohne Programmiererfahrung und entwickelte sich Schritt für Schritt zu einer eigenständigen lokalen Anwendung.

Vielleicht ist EDGAR deshalb nicht perfekt. ( zB 
dauert die Initialisierung des Sprachmodells je nach 
Mac schon
seine Zeit, erst ab der zweiten eingegebenen Frage 
läuft es rund)

Aber genau darum geht es.

Ausprobieren. Lernen. Verändern. Selber machen.

## Ausführbare Datei erstellen

Voraussetzungen:
- Python 3.14 oder neuer
- PyInstaller

Im Terminal in den Projektordner wechseln:

```bash
cd /Pfad/zu/Edgar
```

PyInstaller installieren:

```bash
python3 -m pip install pyinstaller
```

Ausführbare Datei erstellen:

```bash
python3 -m PyInstaller --onefile Edgar1.py
```

Die fertige ausführbare Datei befindet sich anschließend im Ordner mit den Codedateien:

/dist 

`mimir_engine.py` und `mimir_model_manager.py` müssen sich beim Erstellen im selben Projektordner wie `Edgar1.py` befinden. PyInstaller bindet die von `Edgar1.py` verwendeten Python-Dateien automatisch ein.

Die ausführbare Datei startet direkt das Terminal. Beim Erststart wirst du gefragt, ob du das Sprachmodell downloaden möchtest. Ohne geht es leider nicht.





Viel Spaß mit EDGAR!
