
from flaskApp import socketio,bus
from flask import request

class ReceiveClass:

    @classmethod
    @socketio.on('signUp')
    def signUp(data):
        print(data)
        bus.emit('signUp',data,request.sid)

    @classmethod
    @socketio.on('receiveEval')
    def receive(data):
        print(data)
        bus.emit('receiveEval',data,request.sid)

    @classmethod
    @socketio.on('login')
    def login(data):
        bus.emit('login',data,request.sid)
    
    @classmethod
    @socketio.on('logout')
    def logout(data):
        print(data)
        bus.emit('logout',data,request.sid)
    
    @classmethod
    @socketio.on('sponsors')
    def sponsors(type):
        print(type)
        bus.emit('sponsorsBus',type,request.sid)
    
    @classmethod
    @socketio.on('eventsReq')
    def events():
        bus.emit('eventsBus',request.sid)