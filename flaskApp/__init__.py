from flask import Flask,jsonify,Request
from flask_sqlalchemy import SQLAlchemy

from flask_socketio import SocketIO
app=Flask(__name__)
app.config['SECRET_KEY'] = '18da407c0c7205283d9e0ecb512e3ef9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins='http://localhost:8080')

klijenti=[]
from flaskApp import routes