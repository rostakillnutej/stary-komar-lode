from flask import request, send_from_directory
from lode import app, socketio
#from lode.controllers import user, reminder, note, task

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

'''
@app.route('/lobby/new', methods=['POST'])
def createLobby():
    return lobby.create(request)

@app.route('/lobby', methods=['GET'])
def getLobby():
    return lobby.get(request)
'''

'''
@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

###################################

@socketio.on('change')
def on_change(data):
    print('-------------');
    print(data);
    print('-------------');
    emit('change_response', data, broadcast=True)
'''
