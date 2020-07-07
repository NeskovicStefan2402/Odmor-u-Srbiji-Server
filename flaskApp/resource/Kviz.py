from flaskApp.models.Kviz import Kviz,Pitanje,Odgovor,Nagrada
from flaskApp import socketio,bus
from flaskApp.resource.Destinacija import Destinacija
from flaskApp.ResponseObject import ResponseObject
class KvizResource():

    @classmethod
    def dodajKviz(cls,data):
        try:
            pitanja = data['pitanja']
            nagrade = data['nagrade']
            kviz = Kviz(data['datum'],data['destinacija'])
            kviz.add()
            for i in pitanja:
                pitanje = Pitanje(i['text'],kviz.id)
                pitanje.add()
                for j in i['odgovori']:
                    odgovor = Odgovor(j['text'],j['tacan'],pitanje.id)
                    odgovor.add()
            for i in nagrade:
                KvizResource.dodajNagradu(i,kviz.id)
            socketio.emit('insert_quiz')
            return {'Odgovor':'Uspesno je kreiran kviz!'}    
        except Exception as e:
            return {'Greska':'Rip greske : '+e.args[0]}
        
    @classmethod
    def vratiKviz(cls,id):
        kviz= Kviz.vrati_kviz(id).json()
        kviz['brojPitanja']=Pitanje.vrati_sve_za_kviz(id).count()
        nagrade=[]
        for i in Nagrada.vrati_sve_za_kviz(kviz['id']):
            nagrade.append(i.json())
        kviz['nagrade']=nagrade
        kviz['tema'] = Destinacija.vrati_id(kviz['destinacija']).naziv
        return kviz
    
    @classmethod
    def dodajNagradu(cls,data,kviz):
        try:
            nagrada = Nagrada(data['naziv'],data['iznos'],data['rank'],data['sponzor'],kviz)
            nagrada.add()
            return {'Odgovor':'Uspesno je dodata nagrada za kviz!'}    
        except Exception as e:
            return {'Greska':'Rip greske : '+e.args[0]}

    @classmethod
    def vratiOdgovor(cls,id):
        return Odgovor.vrati_odgovor(id).json() 

    @classmethod
    def vratiNagrade(cls,kviz):
        try:
            nagrade = Nagrada.vrati_sve_za_kviz(kviz)
            results=[]
            for i in nagrade:
                results.append(i.json())
            return {'Odgovor':results}    
        except Exception as e:
            return {'Greska':'Rip greske : '+e.args[0]}
    
# -----------------------------------------------
    @bus.on('eventsBus')       
    def vratiRasporedKvizova(sid):
        try:
            obj=ResponseObject(None,None)
            kvizovi = Kviz.vrati_sve()
            result=[]
            for i in kvizovi:
                kviz=KvizResource.vratiKviz(i.id)
                result.append(kviz)
            obj.objekat=result
        except Exception as e:
            obj.error= str(e)
        bus.emit('eventsResp',obj.json(),sid)
# -----------------------------------------------
    