class Flugplatz:
    def __init__(self, name, max_flugzeuge):
        self.name = name
        self.max_flugzeuge = max_flugzeuge
        self.flugzeuge = []

    def add_flugzeug(self, flugzeug):
        if len(self.flugzeuge) < self.max_flugzeuge:
            self.flugzeuge.append(flugzeug)
            print("Flugzeug erfolgreich hinzugefügt.")
        else:
            print("Maximale Anzahl an Flugzeugen erreicht.")
            
'''
Klasse für Flugzeugträger. Hat Liste mit Flugzeugen, maximale Anzahl, sowie Funktionen
zum Hinzufügen und starten von Flugzeugen
'''
class Flugzeugtraeger(Flugplatz):
    def __init__(self, name, kapazitaet, max_flugzeuge):
        Flugplatz.__init__(self, name, max_flugzeuge)
        self.kapazitaet=kapazitaet

    #Entfernt Flugzeug von Liste und startet es
    def starte_flugzeug(self, flugzeug):
        if flugzeug in self.flugzeuge:
            print("Flugzeug", flugzeug.name ,"startet...")
            # Simuliere Startvorgang
            self.flugzeuge.remove(flugzeug)
            print("Flugzeug", flugzeug.name ,"gestartet.")
        else:
            print("Flugzeug nicht gefunden.")
        
class Flugzeug:
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht
        
# Beispielinstanz erzeugen
traeger = Flugzeugtraeger("Aircraft Carrier", 100000, 50)

flugz=Flugzeug("F-16",1000)
traeger.add_flugzeug(flugz)
traeger.starte_flugzeug(flugz)  # Starten eines Flugzeugs