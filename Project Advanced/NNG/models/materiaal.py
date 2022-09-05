
class Materiaal:

    def __init__(self, naam, omschrijving, atacode, soort, partnummer, serienummer, positie):
        self.naam = naam
        self.omschrijving = omschrijving
        self.atacode = atacode
        self.type = soort
        self.partnummer = partnummer
        self.serienummer = serienummer
        self.positie = positie

    def __repr__(self):
        return ' - '.join(self.__dict__.values())


# --------------------------------------------------------------------

if __name__ == '__main__':

    materieel = []

    materieel.append( Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front') )
    materieel.append( Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel RA', '0023', 'landingsgestel', 'LG893428', '374589-324786', 'rechtsachter') )
    materieel.append( Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893429', '374589-324782', 'linksachter') )
    materieel.append( Materiaal('Landingsgestel F35', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893129', '474589-324782', 'front') )

    for materiaal in materieel:
        if 'F16' in materiaal.naam:
            print(materiaal)

