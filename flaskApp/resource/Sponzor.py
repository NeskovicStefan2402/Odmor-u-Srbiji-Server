from flaskApp.models.Sponzor import Level,Sponzor
from flaskApp.resource.Destinacija import ResourceDestinacija
from flaskApp.ResponseObject import ResponseObject
from flaskApp import bus

class SponzorResource:

    @classmethod
    def unesi_sponzora(cls,data):
        try:
            koordinate = ResourceDestinacija.vratiKoordinate(data['destinacija'])
            sponzor = Sponzor(data['naziv'],data['destinacija'],data['iznos'],data['opis'],koordinate[0],koordinate[1],data['slika'])
            sponzor.add()
            return {'Odgovor':'Uspesno je sacuvan sponzor '+sponzor.naziv}
        except Exception as e:
            return {'Greska': e.args[0]}

    @classmethod
    def unesi_level(cls,data):
        try:
            level = Level(data['naziv'],data['gornja'],data['donja'])
            level.add()
            return {'Odgovor':'Uspesno je sacuvan level.'}
        except Exception as e:
            return { 'Greska' : e.args[0] }
# -----------------------------------------------------
    @bus.on('sponsorsBus')
    def vrati_sponzore(type,sid):
        try:
            obj=ResponseObject(None,None)
            sponzori = Sponzor.vrati_sve_level(type)
            result = []
            for i in sponzori:
                result.append(i.json())
            obj.objekat=result
        except Exception as e:
            obj.error= str(e)
        bus.emit('sponsorsResp',obj.json(),sid)
# -----------------------------------------------------