from flaskApp import db
from datetime import datetime

class Kviz(db.Model):
    __tablename__='Kviz'
    id=db.Column(db.Integer,primary_key=True)
    tema=db.Column(db.String(50))
    datum=db.Column(db.DateTime)

    def __init__(self,tema,datum):
        self.tema=tema
        # '09/19/18 13:55:26' format
        datum = datetime.strptime(datum, '%m/%d/%y %H:%M:%S')
        self.datum=datum
    
    def json(self):
        return {
            'id' : self.id,
            'tema' : self.tema,
            'datum' : self.datum
        }
    
    # @classmethod
    # def pronadji_po_nazivu(cls,naziv):
    #     return cls.query.filter_by(naziv=naziv).first()
    
    @classmethod
    def vrati_kviz(cls,id):
        return cls.query.filter_by(id=id).first()
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Pitanje(db.Model):
    __tablename__='Pitanje'
    id=db.Column(db.Integer,primary_key=True)
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
    id=db.Column(db.Integer,primary_key=True)
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