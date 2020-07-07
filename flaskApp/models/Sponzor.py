from flaskApp import db
from datetime import datetime
from flaskApp.models.Destinacija import Destinacija

class Sponzor(db.Model):
    __tablename__='Sponzor'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    naziv = db.Column(db.String(50))
    iznos = db.Column(db.Float())
    slika = db.Column(db.String(1000))
    opis =  db.Column(db.String(1000))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    level_id = db.Column(db.Integer, db.ForeignKey('Level.id'),nullable=False)
    destinacija_id = db.Column(db.Integer, db.ForeignKey('Destinacija.id'),nullable=False)
    
    def __init__(self,naziv,destinacija,iznos,opis,lat,lng,slika):
        self.naziv=naziv
        self.destinacija_id=Destinacija.vrati_naziv(destinacija).json()['id']
        self.iznos=iznos
        self.slika=slika
        self.opis=opis
        self.lat=lat
        self.lng=lng
        self.level_id= Level.vrati_level(iznos).json()['id']
    
    def json(self):
        return {
            'id' : self.id,
            'naziv' : self.naziv,
            'destinacija' : self.destinacija_id,
            'lat' : self.lat,
            'lng' : self.lng,
            'slika': self.slika,
            'opis' : self.opis,
            'level' : self.level_id
            }
    
    @classmethod
    def vrati_sponzor(cls,id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def vrati_sve_level(cls,naziv):
        level = Level.vrati_naziv(naziv)
        return cls.query.filter(Sponzor.level_id==level.id).all()

    @classmethod
    def vrati_sve(cls):
        return cls.query.all()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Level(db.Model):
    __tablename__='Level'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    naziv = db.Column(db.String(50))
    donja_granica= db.Column(db.Float())
    gornja_granica= db.Column(db.Float())

    def __init__(self,naziv,gornja,donja):
        self.naziv=naziv
        self.gornja_granica=gornja
        self.donja_granica=donja
        
    def json(self):
        return {
            'id' : self.id,
            'naziv' : self.naziv,
            'donja_granica' : self.donja_granica,
            'gornja_granica' : self.gornja_granica
            }
    
    @classmethod
    def vrati_level(cls,iznos):
        result=cls.query.filter(Level.donja_granica<iznos).filter(Level.gornja_granica>=iznos).first()
        return result
    
    @classmethod
    def vrati_naziv(cls,naziv):
        return cls.query.filter_by(naziv=naziv).first()

    @classmethod
    def vrati_sve(cls):
        return cls.query.all()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

