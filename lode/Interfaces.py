from flask import request, send_from_directory
from flask_socketio import send, emit
from lode import app, socketio
from lode.controllers import Lobby, ShipAi
from lode.models.Ship import Ship
from lode.models.DraftTable import DraftTable

@app.route('/', methods=['GET'])
def index():
    #return app.send_static_file('index.html')
    pass


@app.route('/game/new', methods=['POST'])
def new():
    print('ok')
    return '',200

#@app.route('/lobby/new', methods=['POST'])
#def createLobby():
#    return lobby.create(request)
ShipAi.randomGrid()
#print(ShipAi.randomGrid())
#ShipAi.gridToStr(ShipAi.randomGrid())

#print(Ship().parseSaveData('Letadlová loď,default,5,1,11111'))

'''
s1 = Ship()
s1.parseSaveData('Letadlová loď,default,5,1,11111')
s2 = Ship()
s2.parseSaveData('Bitevní loď,default,4,1,1111')
s3 = Ship()
s3.parseSaveData('Křižník,default,3,1,111')
s4 = Ship()
s4.parseSaveData('Ponorka,default,3,1,111')
s5 = Ship()
s5.parseSaveData('Torpédoborec,default,2,1,11')


dt = DraftTable(10)
s1.rotate()
dt.placeShip(s1,6,1)
dt.placeShip(s2,1,2)
dt.placeShip(s3,1,4)
dt.placeShip(s4,1,6)
data = dt.getSaveData()
dt2 = DraftTable()
dt2.parseSaveData(data)
print(dt2.getGridString())
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


#@socketio.on('my broadcast event', namespace='/test')
#def test_message(message):
#    emit('my response', {'data': message['data']}, broadcast=True)
