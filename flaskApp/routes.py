from flask import Flask,jsonify,request
from flaskApp import app,db,socketio,klijenti
import time
from flaskApp.resource.Kviz import KvizResource


@app.before_first_request
def create_tables():
    db.create_all()

# @app.route('/getKviz/<id>',methods=['GET'])
# def getFunkcija(id):
#     return jsonify(KvizResource.vratiKviz(int(id)))

# @app.route('/postKviz',methods=['POST'])
# def dodajPitanje():
#     data=request.json
#     return jsonify(KvizResource.dodajKviz(data))

@socketio.on('connect')
def connect_to_server():
    klijenti.append(request.namespace)

@socketio.on('disconnect')
def disconnect_to_server():
    klijenti.remove(request.namespace)

@socketio.on('kontrolni')
def kontrolni(json):
    kviz=KvizResource.vratiKviz(int(json['data']))
    for i in kviz['pitanja']:
        # print(i)
        for j in klijenti:
            j.emit('pitanje',i)
        time.sleep(5)
    return 1

@socketio.on('obicanEvent')
def obican(json):
    print(json)
    return jsonify(KvizResource.vratiKviz(int(json['data'])))

@socketio.on('odgovori')
def odgovori(json):
    if KvizResource.vratiOdgovor(json['odgovor'])['tacan']==False:
        klijenti.remove(request.sid)