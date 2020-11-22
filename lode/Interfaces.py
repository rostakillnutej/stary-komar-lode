from flask import request, send_from_directory
from flask_socketio import send, emit
from lode import app, socketio
from lode.controllers import Lobby
from lode.models.InstanceManager import InstanceManager

'''
@app.route('/', methods=['GET'])
def index():
    #return app.send_static_file('index.html')
    pass
'''

im = InstanceManager()

@socketio.on('connect', namespace='/plan')
def con():
    im.add(request.sid)


@socketio.on('disconnect', namespace='/plan')
def discon():
    im.delete(request.sid)


'''
@socketio.on('connect')
def connect():
    print('connected: ' + request.sid)
    lobby.establish()
    #Když se někdo připojí na socket


@socketio.on('disconnect')
def disconnect():
    print('disconnected: ' + request.sid)
    #Když se někdo odpojí od socketu
'''

#@socketio.on('my broadcast event', namespace='/test')
#def test_message(message):
#    emit('my response', {'data': message['data']}, broadcast=True)
