from flask import Flask,jsonify,Request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS
from event_bus import EventBus

app=Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '18da407c0c7205283d9e0ecb512e3ef9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
CORS(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins='http://localhost:8080')

klijenti=[]
scores=[]

bus= EventBus()

from flaskApp import routes