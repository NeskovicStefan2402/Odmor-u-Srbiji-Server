from flaskApp.models.Kviz import Kviz,Pitanje,Odgovor
from flaskApp import socketio

class KvizResource():

    @classmethod
    def dodajKviz(cls,data):
        try:
            pitanja= data['pitanja']
            kviz = Kviz(data['tema'],data['datum'])
            kviz.add()
            for i in pitanja:
                pitanje = Pitanje(i['text'],kviz.id)
                pitanje.add()
                for j in i['odgovori']:
                    odgovor = Odgovor(j['text'],j['tacan'],pitanje.id)
                    odgovor.add()
            socketio.emit('insert_quiz')
            return {'Odgovor':'Uspesno je kreiran kviz!'}    
        except Exception as e:
            return {'Greska':'Rip greske : '+e.args[0]}
        
    @classmethod
    def vratiKviz(cls,id):
        kviz= Kviz.vrati_kviz(id).json()
        pitanja=[]
        for i in Pitanje.vrati_sve_za_kviz(id):
            pitanja.append(i.json())
        kviz['pitanja']=pitanja
        for i in pitanja:
            odgovori=[]
            for j in Odgovor.vrati_sve_za_pitanje(i['id']):
                odgovori.append(j.json())
            i['odgovori']=odgovori
        return kviz
    
    @classmethod
    def vratiOdgovor(cls,id):
        return Odgovor.vrati_odgovor(id).json() 
            