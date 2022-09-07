import jsonpickle

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///nng.db', echo=True)
Base = declarative_base()

class Gebeurtenis(Base):

    __tablename__ = "gebeurtennis"

    id = Column(Integer, primary_key=True)
    intensiteit = Column(String)
    datum = Column(String)
    betrokken_gebruiker = Column(String)
    omschrijving = Column(String)
    locatie = Column(String)
    omstandigheden = Column(String)
    materiaal_id = Column(Integer, ForeignKey("materiaal.id"))

    def __init__(self, intensiteit, datum, betrokken_gebruiker, omschrijving, locatie, omstandigheden):
        self.intensiteit = intensiteit
        self.datum = datum
        self.betrokken_gebruiker = betrokken_gebruiker
        self.omschrijving = omschrijving
        self.locatie = locatie
        self.omstandigheden = omstandigheden

    def __repr__(self):
        return ' - '.join(self.__dict__.values())

    def overzicht(self) -> str:
        return f'{self.datum} - {self.omschrijving}'

    def to_json(self):
        return jsonpickle.dumps(self)

# --------------------------------------------------------------------

if __name__ == '__main__':

    gebeurtenisen = []

    gebeurtenisen.append( Gebeurtenis('**', '2022-09-05', 'Peter', 'Harde landing', 'Soesterberg', 'windkracht 7 zijwaarts') )
    gebeurtenisen.append( Gebeurtenis('***', '2022-09-06', 'Peter', 'Zeer harde landing', 'Soesterberg', 'windkracht 7 frontaal') )

    for gebeurtenis in gebeurtenisen:
        print(gebeurtenis)
