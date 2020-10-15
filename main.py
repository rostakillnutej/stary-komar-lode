from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, emit
import logging,sys

sys.path.append('./controllers')
import lobby

logging.getLogger('werkzeug').setLevel(logging.ERROR)


app = Flask(__name__, static_url_path='', static_folder='public')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'tajny kodes na šifry tady'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/lobby/new', methods=['POST'])
def createLobby():
    return lobby.create(request)

@app.route('/lobby', methods=['GET'])
def getLobby():
    return lobby.get(request)

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

if __name__ == '__main__':
    socketio.run(app)
    app.run(host= '0.0.0.0')
