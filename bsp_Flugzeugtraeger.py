'''
Klasse für Flugzeugträger. Hat Liste mit Flugzeugen, maximale Anzahl, sowie Funktionen
zum Hinzufügen und starten von Flugzeugen
'''
class Flugzeugtraeger:
    def __init__(self, name, max_flugzeuge):
        self.name = name
        self.max_flugzeuge = max_flugzeuge
        self.flugzeuge = []

    #Entfernt Flugzeug von Liste und startet es
    def starte_flugzeug(self, flugzeug):
        if flugzeug in self.flugzeuge:
            print("Flugzeug", flugzeug ,"startet...")
            # Simuliere Startvorgang
            self.flugzeuge.remove(flugzeug)
            print("Flugzeug", flugzeug ,"gestartet.")
        else:
            print("Flugzeug nicht gefunden.")
        
    # Fügt Flugzeug hinzu, falls maximalanzahl noch nicht erreicht
    def add_flugzeug(self, flugzeug):
        if len(self.flugzeuge) < self.max_flugzeuge:
            self.flugzeuge.append(flugzeug)
            print("Flugzeug erfolgreich hinzugefügt.")
        else:
            print("Maximale Anzahl an Flugzeugen erreicht.")

# Beispielinstanz erzeugen
traeger = Flugzeugtraeger("Aircraft Carrier", 50)

traeger.add_flugzeug("F-16")
traeger.starte_flugzeug("F-16")  # Starten eines Flugzeugs