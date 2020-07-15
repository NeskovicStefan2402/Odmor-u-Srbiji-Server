from flaskApp import db
from datetime import datetime
from flaskApp.models.Sponzor import Sponzor
from flaskApp.models.Korisnik import Korisnik
from flaskApp.models.Destinacija import Destinacija

class Kviz(db.Model):
    __tablename__='Kviz'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    datum=db.Column(db.DateTime)
    destinacija_id = db.Column(db.Integer, db.ForeignKey('Destinacija.id'),nullable=False)

    def __init__(self,datum,destinacija):
        # '09/19/18 13:55:26' format
        datum = datetime.strptime(datum, '%m/%d/%y %H:%M:%S')
        self.datum=datum
        self.destinacija_id=destinacija
    
    def json(self):
        return {
            'id' : self.id,
            'datum' : self.datum.strftime('%m/%d/%y %H:%M:%S'),
            'vreme':str(self.datum.hour)+':'+str(self.datum.minute),
            'destinacija':self.destinacija_id
        }
    
    @classmethod
    def vrati_kviz(cls,id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def vrati_sve(cls):
        return cls.query.filter(Kviz.datum>datetime.now()).all()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Pitanje(db.Model):
    __tablename__='Pitanje'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    text=db.Column(db.String(50))
    kviz_id = db.Column(db.Integer, db.ForeignKey('Kviz.id'),nullable=False)

    def __init__(self,text,kviz_id):
        self.text=text
        self.kviz_id=kviz_id
    
    def json(self):
        return {
            'id' : self.id,
            'text' : self.text,
            'kviz' : self.kviz_id
        }

    @classmethod
    def vrati_sve_za_kviz(cls,id):
        return cls.query.filter_by(kviz_id=id)
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Odgovor(db.Model):
    __tablename__='Odgovor'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    text = db.Column(db.String(50))
    tacan = db.Column(db.Boolean())
    pitanje_id = db.Column(db.Integer, db.ForeignKey('Pitanje.id'),nullable=False)

    def __init__(self,text,tacan,pitanje_id):
        self.text=text
        self.tacan=tacan
        self.pitanje_id=pitanje_id
    
    def json(self):
        return {
            'id' : self.id,
            'text' : self.text,
            'tacan':self.tacan,
            'pitanje': self.pitanje_id
        }
    @classmethod
    def vrati_sve_za_pitanje(cls,id):
        return cls.query.filter_by(pitanje_id=id)

    @classmethod
    def vrati_odgovor(cls,id):
        return cls.query.filter_by(id=id).first()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Nagrada(db.Model):
    __tablename__='Nagrada'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    naziv = db.Column(db.String(50))
    iznos = db.Column(db.Float())
    rank = db.Column(db.Integer)
    korisnik_id = db.Column(db.Integer, db.ForeignKey('Korisnik.id'),nullable=True)
    sponzor_id = db.Column(db.Integer, db.ForeignKey('Sponzor.id'),nullable=False)
    kviz_id = db.Column(db.Integer, db.ForeignKey('Kviz.id'),nullable=False)

    def __init__(self,naziv,iznos,rank,sponzor_id,kviz_id):
        self.naziv=naziv
        self.iznos=iznos
        self.rank=rank
        self.korisnik_id=None
        self.sponzor_id = sponzor_id
        self.kviz_id = kviz_id 
    
    def json(self):
        return {
            'id' : self.id,
            'naziv' : self.naziv,
            'iznos' : self.iznos,
            'rank' : self.rank,
            'dobitnik' : None if self.korisnik_id==None else Korisnik.vrati_korisnik(self.korisnik_id).json(),
            'sponzor' : Sponzor.vrati_sponzor(self.sponzor_id).naziv
        }

    @classmethod
    def vrati_sve_za_kviz(cls,id):
        return cls.query.filter_by(kviz_id=id)
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,korisnik_id):
        self.korisnik_id=korisnik_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
