from flaskApp import db
from flaskApp.models.Korisnik import Korisnik
from flaskApp.models.Kviz import Kviz

class Rezultat(db.Model):
    __tablename__='Rezultat'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    kviz_id = db.Column(db.Integer, db.ForeignKey('Kviz.id'),nullable=False)
    korisnik_id = db.Column(db.Integer, db.ForeignKey('Korisnik.id'),nullable=False)
    vrednost = db.Column(db.Float())

    def __init__(self,kviz,korisnik,vrednost):
        self.korisnik_id=korisnik
        self.kviz_id=kviz
        self.vrednost=vrednost
    
    def json(self):
        return {
            'id':self.id,
            'korisnik':self.korisnik_id,
            'kviz':self.kviz_id,
            'vrednost':self.vrednost,
            }
    
    @classmethod
    def vrati_rezultate_za_kviz(cls,id):
        return cls.query.filter_by(kviz_id=id)
    
    @classmethod
    def vrati_rezultate_za_korisnik(cls,id):
        return cls.query.filter_by(korisnik_id=id)
    
    @classmethod
    def vrati_sve(cls):
        return cls.query.all()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

