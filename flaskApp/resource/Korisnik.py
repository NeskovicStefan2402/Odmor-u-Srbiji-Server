from flaskApp.models.Korisnik import Korisnik
from flaskApp import bus,resource,Send,Receive
from flaskApp.Other import OtherMethods
from flaskApp.ResponseObject import ResponseObject
import random
class KorisnikResource:

    @bus.on('signUp')
    def unesiKorisnika(data,sid):
        try:
            security = random.randint(100000,999999)
            korisnik = Korisnik(data['phone'],data['password'],security)
            data=OtherMethods.read_json()
            obj=korisnik.json()
            obj['security']=security
            data.append(obj)
            OtherMethods.write_json(data)
            bus.emit('sendMessage',korisnik)
            bus.emit('evaluate',korisnik.json(),sid)
            return {'Odgovor':'Korisnik je uspesno kreiran'} 
        except Exception as e:
            print(e)
            return {'Greska':e.args[0]}
    
    @bus.on('receiveEval')
    def verifikujKorisnika(data,sid):
        try:
            obj=ResponseObject(None,None)
            kor = OtherMethods.get_object(data['phone'])
            if int(data['security']) == int(kor['security']):
                korisnik = Korisnik(kor['phone'],kor['password'],kor['security'])
                korisnik.add()
                obj.objekat=korisnik.json()
            else:
                obj.objekat=None
                obj.error='Evaluacija'  
        except Exception as e:
            obj.objekat=None
            obj.error=str(e)
        OtherMethods.delete_object(data['phone'])
        bus.emit('confirmEvaluation',obj.json(),sid)  

    @bus.on('login')
    def prijaviKorisnika(data,sid):
        try:
            obj=ResponseObject(None,None)
            print('Data je : ')
            print(data['phone'])
            print(data['password'])
            korisnik = Korisnik.nadji_korisnika(data['phone'],data['password'])
            print('Korinsik je : ')
            
            if korisnik==None:
                obj.error='Korisnik ne postoji u bazi'
            elif korisnik.ulogovan==True:
                obj.error='Korisnik je ulogovan na drugom uredjaju'
            else:
                korisnik.prijavi()
                obj.objekat=korisnik.json() 
        except Exception as e:
            obj.error=str(e)
        bus.emit('evaluateLogin',obj.json(),sid)

    @bus.on('logout')
    def odjaviKorisnika(data,sid):
        try:
            print(data)
            obj=ResponseObject(None,None)
            korisnik = Korisnik.nadji_korisnika(data['phone'],data['password'])
            if korisnik==None:
                obj.error='Korisnik ne postoji u bazi'
            elif korisnik.ulogovan==False:
                obj.error='Korisnik nije ulogovan!'
            else:
                korisnik.odjavi()
                obj.objekat=korisnik.json() 
        except Exception as e:
            obj.error=str(e)
        bus.emit('evaluateLogout',obj.json(),sid)
# --------------------------------------------------------
    @classmethod
    def dodajPoene(cls,id,score):
        try:
            korisnik = Korisnik.vrati_korisnik(id)
            korisnik.update(score)
            return {'Odgovor':'Korisniku su uspesno dodati poeni!'} 
        except Exception as e:
            return {'Greska':e.args[0]}

    
    
    