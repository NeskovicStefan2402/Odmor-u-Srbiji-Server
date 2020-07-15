from flaskApp import socketio,bus,klijenti,scores
import time
from flaskApp.Other import OtherMethods
from flaskApp.resource.Rezultat import RezultatResource

class SendClass:

    @bus.on('evaluate')
    def signUp(data,sid):
        socketio.emit('eval',data,room=sid)
    
    @bus.on('confirmEvaluation')
    def signUpEval(data,sid):
        socketio.emit('confirmEvaluation',data,room=sid)
    
    @bus.on('evaluateLogin')
    def evaluateLogin(data,sid):
        socketio.emit('evaluateLogin',data,room=sid)
    
    @bus.on('evaluateLogout')
    def evaluateLogout(data,sid):
        socketio.emit('evaluateLogout',data,room=sid)
    
    @bus.on('sponsorsResp')
    def sponsorsResp(data,sid):
        socketio.emit('responseSponsors',data,room=sid)

    @bus.on('eventsResp')
    def eventsResp(data,sid):
        socketio.emit('responseEvents',data,room=sid)
    
    @bus.on('addNotification')
    def notification(data):
        socketio.emit('notification',data)

    @bus.on('loadingQuiz')
    def loadingQuiz(kviz_id):
        socketio.emit('loadingQuiz',kviz_id)

    @bus.on('uploadQuiz')
    def uploadQuiz(kviz):
        sids=[i['sid'] for i in klijenti]
        for i in sids:
            socketio.emit('uploadQuiz',kviz,room=i)
        time.sleep(10*len(kviz['objekat']['pitanja']))
        sids=[i['sid'] for i in klijenti]
        for i in sids:
            socketio.emit('endQuiz',room=i)
        time.sleep(3)
        print(OtherMethods.vrati_rang_listu())
        RezultatResource.unesiRezultateKviza(kviz['objekat']['id'])
        notification='Izvrsene su izmene na rang listi'
        bus.emit('addNotification',notification)
        scores=[]
        # klijenti=[]
        