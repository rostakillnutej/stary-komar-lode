#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_socketio import SocketIO
import logging
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cors = CORS(app, resources={"*": {"supports_credentials": "true"}})

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/main.sqlite3'
app.config['SECRET_KEY'] = 'toto-sifruje-websocket-komunikaci'
socketio = SocketIO(app,cors_allowed_origins="*")
DB = SQLAlchemy(app)


from lode import Interfaces
