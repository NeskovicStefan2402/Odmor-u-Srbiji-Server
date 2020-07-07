from twilio.rest import Client
from flaskApp import bus
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