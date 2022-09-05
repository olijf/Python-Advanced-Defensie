
class Onderhoud:

    def __init__(self, naam, datum, door_wie, bevindingen):
        self.type = naam
        self.datum = datum
        self.door_wie = door_wie
        self.bevindingen = bevindingen
        self.onderdelen = []
        self.verbruiksmiddelen = []
        self.tooling = []

    def __repr__(self):
        return ' - '.join(self.__dict__.values())


# --------------------------------------------------------------------

if __name__ == '__main__':

    onderhoudsbeurten = []

    onderhoudsbeurten.append( Onderhoud('Inspectie', '2022-09-05', 'Peter', 'OK') )
    onderhoudsbeurten.append( Onderhoud('Regulier onderhoud', '2022-09-05', 'Peter', 'OK') )
    onderhoudsbeurten.append( Onderhoud('Regulier onderhoud', '2022-08-05', 'Peter', 'OK') )
    onderhoudsbeurten.append( Onderhoud('Spoed onderhoud', '2022-08-15', 'Peter', 'OK') )

    for onderhoud in onderhoudsbeurten:
        print(onderhoud)

