from twilio.rest import Client
from flaskApp.models.Kviz import Kviz,Pitanje,Odgovor
from flaskApp import bus,scores,klijenti
import json
class OtherMethods:

    @classmethod
    def izracunajRezultat(data):
        pass

    @bus.on('sendMessage')
    def posaljiSMS(korisnik):
        print('Messages')
        account_sid = 'ACdd6228b2d26cf6c85d0c55ac7509ec27'
        auth_token = '20d989fcc18b2b91adef508de423ef67'
        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(body='Your security code is : '+str(korisnik.security),from_='+12032023466',to='+381616202600')

    @classmethod
    def write_json(cls,data): 
        with open('privremena.txt','w') as f: 
            json.dump(data, f) 
    
    @classmethod
    def read_json(cls):
        with open('privremena.txt') as json_file: 
            data = json.load(json_file)
            print(data) 
        return data

    @classmethod
    def get_object(cls,phone):
        with open('privremena.txt') as json_file: 
            data = json.load(json_file) 
        obj=None
        for i in data:
            if i['phone']==phone:
                obj=i
        return obj
    
    @classmethod
    def delete_object(cls,phone):
        with open('privremena.txt') as json_file: 
            data = json.load(json_file) 
        for i in data:
            if i['phone']==phone:
                data.remove(i)
        OtherMethods.write_json(data)

    @classmethod
    def zapisiRezultat(cls,kviz_id,obj):
        pitanja = Pitanje.vrati_sve_za_kviz(kviz_id)
        suma=0
        for i in obj['answers']:
            print('Usao u answer ')
            print(pitanja[i['pitanje']-1].json())
            odgovori = Odgovor.vrati_sve_za_pitanje(pitanja[i['pitanje']-1].id)
            if odgovori[i['odgovor']-1].tacan == True:
                suma+=1
                print('True '+str(suma))
            elif odgovori[i['odgovor']-1].tacan == False:
                suma+=2
                print('False '+str(suma))
        score={
            'user': OtherMethods.get_user(obj['sid'])['user'],
            'score':suma*obj['time']
        }
        scores.append(score)
        klijenti.remove(OtherMethods.get_user(obj['sid']))
        print(scores)

    @classmethod
    def get_user(cls,sid):
        for i in klijenti:
            if i['sid']==sid:
                return i
        return None
    
    @classmethod
    def vrati_rang_listu(cls):
        try:
            scores.sort(key=lambda x: x['score'])
            return scores
        except Exception as e:
            print(e)
            return []