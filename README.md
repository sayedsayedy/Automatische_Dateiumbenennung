# Automatische Dateiumbenennung

![alt text](Screenshot.png)


## Beschreibung

Dieses Projekt enthält ein Python-Skript und eine ausführbare `.exe`-Datei zur automatischen Umbenennung von Gehaltsabrechnungen und Meldebescheinigungen für Mitarbeitende. Die Anwendung verwendet eine grafische Benutzeroberfläche (GUI) zur Auswahl einer CSV-Datei und des Ordners mit den umzubenennenden Dateien.



## Funktionen

- **Automatisches Umbenennen von Dateien:**

  - Gehaltsabrechnungen: `Personalnummer_Vorname_Nachname_Gehaltsabrechnung_ddmmyyyy.pdf`

  - Meldebescheinigungen: `Personalnummer_Vorname_Nachname_Meldebescheinigung Sozialversicherung_ddmmyyyy.pdf`

- **GUI** für einfache Bedienung

- **Eigenständige `.exe`-Datei**, die ohne Python-Installation funktioniert



## Dateien

- `Automatische_Dateiumbenennung.py`: Python-Skript mit der Hauptlogik

- `Dateiumbenennung.exe`: Ausführbare Datei



## CSV-Datei

Die CSV-Datei muss folgende Spalten enthalten:

- **Personalnummer**

- **Vorname**

- **Nachname**



Beispiel:



Personalnummer,Vorname,Nachname

123,Max,Mustermann

456,Lisa,Müller

789,Sayed,Sayedy



## Anforderungen

- **Python-Bibliotheken** (für die Python-Version der Anwendung):

  - `Pandas`

  - `tkinter`

  - `Pillow`

## Entwickler

- **Sayed Sayedy** [sayedy.com](https://sayedy.com)
