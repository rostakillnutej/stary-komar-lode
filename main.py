from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

@app.route('/')
def hello_world():
    return 'Hello, World!'
