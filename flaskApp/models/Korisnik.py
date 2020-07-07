from flaskApp import db
from datetime import datetime

class Korisnik(db.Model):
    __tablename__='Korisnik'
    id=db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    ulogovan = db.Column(db.Boolean())
    score = db.Column(db.Float())
    security = db.Column(db.Integer) 

    def __init__(self,phone,password,security):
        self.phone=phone
        self.password=password
        self.score=0
        self.ulogovan=False
        self.security = security

    def json(self):
        return {
            'id': self.id,
            'phone':self.phone,
            'password':self.password,
            'ulogovan':self.ulogovan,
            'score':self.score
        }

    @classmethod
    def vrati_rang_listu(cls):
        return cls.query.all()

    @classmethod
    def vrati_korisnik(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def nadji_korisnika(cls,phone,password):
        ele = cls.query.filter_by(phone=phone).first()
        if ele == None:
            return None
        return ele if ele.password==password else None

    def odjavi(self):
        self.ulogovan=False
        db.session.commit()

    def prijavi(self):
        self.ulogovan=True
        db.session.commit()

    def update(self,new_score):
        self.score+=new_score
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Lokacija(db.Model):
    __tablename__='Lokacija'
    id=db.Column(db.Integer,primary_key=True)
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    vreme = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    korisnik_id = db.Column(db.Integer, db.ForeignKey('Korisnik.id'),nullable=False)

    def __init__(self,lat,lng,korisnik_id):
        self.lat=lat
        self.lng=lng
        self.korisnik_id = korisnik_id

    def json(self):
        return {
            'id': self.id,
            'lat':self.lat,
            'lng':self.lng,
            'vreme':self.vreme,
            'korisnik':self.korisnik_id
        }

    def update(self,new_score):
        self.score+=new_score
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()