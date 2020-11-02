#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO
import logging,sys


logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__, static_url_path='', static_folder='public')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'tajny kodes na šifry tady'
socketio = SocketIO(app)

from lode import interfaces
