from flask import Flask,jsonify,request,send_from_directory
from flaskApp import app,db,socketio,bus,klijenti
import time
from flaskApp.resource.Kviz import KvizResource
from flaskApp.resource.Sponzor import SponzorResource
from flaskApp.resource.Destinacija import ResourceDestinacija
from flaskApp.resource.Korisnik import KorisnikResource


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.static_folder,
                               filename)

@app.route('/postSponsor',methods=['POST'])
def post_sponsor():
    data=request.json
    return SponzorResource.unesi_sponzora(data)

@app.route('/postNagrada',methods=['POST'])
def post_nagrada():
    data=request.json
    return SponzorResource.unesi_sponzora(data)

@app.route('/rangLista')
def rang_lista():
    return KorisnikResource.vrati_rang_listu()

@app.route('/postLevel',methods=['POST'])
def post_level():
    data=request.json
    return SponzorResource.unesi_level(data)

@app.route('/postDestinacija',methods=['POST'])
def post_destinacija():
    data=request.json
    return ResourceDestinacija.unesiDestinaciju(data)

@app.route('/postKviz',methods=['POST'])
def zakaziKviz():
    data=request.json
    return jsonify(KvizResource.dodajKviz(data))

@app.route('/loadingTest')
def loading():
    klijenti=[]
    bus.emit('loadingQuiz',1)
    return 'Loading quiz...'

@app.route('/uploadQuizTest')
def uploadTest():
    bus.emit('uploadQuizTest',1)
    return 'Uploading quiz...'

