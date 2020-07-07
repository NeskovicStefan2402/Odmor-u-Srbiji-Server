from flaskApp import db

class Destinacija(db.Model):
    __tablename__='Destinacija'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    naziv = db.Column(db.String(50))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())

    def __init__(self,naziv,lat,lng):
        self.naziv=naziv
        self.lat=lat
        self.lng=lng

    def json(self):
        return {
            'id' : self.id,
            'naziv' : self.naziv,
            'lat' : self.lat,
            'lng' : self.lng,
            }
    
    @classmethod
    def vrati_naziv(cls,name):
        print('Naziv destinacije za pretragu je : '+name)
        return cls.query.filter(Destinacija.naziv.like(name)).first()
    
    @classmethod
    def vrati_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()