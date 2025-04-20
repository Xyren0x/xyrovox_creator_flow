import time
from datetime import datetime as DatumUhrzeit
import json
import os

# Simulierter Aufgabenplan (wird später dynamisch generiert)
aufgabenliste = [
    {"zeit": "08:00", "aktion": "neue_idee_generieren"},
    {"zeit": "12:00", "aktion": "content_evaluieren"},
    {"zeit": "15:00", "aktion": "feedback_analysieren"},
    {"zeit": "19:00", "aktion": "upload_vorbereitet"}
]

def Protokoll(text):
    zeitstempel = DatumUhrzeit.now().isoformat()
    with open("xyrovox_log.txt", "a") as logfile:
        logfile.write(f"[{zeitstempel}] {text}\n")
    print(f"[{zeitstempel}] {text}")

def neue_idee_generieren():
    Protokoll("Neue Idee generiert – z. B. 'KI erklärt Social Media'")

def content_evaluieren():
    Protokoll("Bewertung vorhandener Inhalte durchgeführt")

def feedback_analysieren():
    Protokoll("Noch kein echtes Feedback – Dummy ausgewertet")

def upload_vorbereitet():
    Protokoll("Upload simuliert – kein echter Upload")

def Schleife():
    while True:
        aktuelle_zeit = DatumUhrzeit.now().strftime("%H:%M")
        for aufgabe in aufgabenliste:
            if aufgabe["zeit"] == aktuelle_zeit:
                aktion = aufgabe["aktion"]
                if aktion == "neue_idee_generieren":
                    neue_idee_generieren()
                elif aktion == "content_evaluieren":
                    content_evaluieren()
                elif aktion == "feedback_analysieren":
                    feedback_analysieren()
                elif aktion == "upload_vorbereitet":
                    upload_vorbereitet()
        time.sleep(60)

if __name__ == "__main__":
    Protokoll("Xyrovox gestartet")
    Schleife()
