from flask import request, send_from_directory
from flask_socketio import send, emit
from lode import app, socketio
from lode.controllers import Lobby
from lode.models import ShipAi
#from lode.models.Ship import Ship
#from lode.models.DraftTable import DraftTable
from lode.models.GameTable import GameTable

from lode.models.PlanInstance import PlanInstance

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



gt = GameTable(ShipAi.randomGrid())
print(gt.getGridString())

pi = PlanInstance()

pi.handleShipRotate(0)
pi.handleShipRotate(1)
pi.handleShipRotate(2)
pi.handleShipRotate(3)

pi.handlePlace(0,0,0)
pi.handlePlace(0,2,3)
pi.handlePlace(0,2,5)
pi.handlePlace(0,2,7)
pi.handlePlace(0,2,9)
print(pi.table.getGridString())
pi.handleRemove(1)
pi.handleRemove(2)
pi.handleRemove(3)
pi.handleRemove(4)
pi.handleRemove(5)
print(pi.table.getGridString())
#print(gt.getGridString())




#if gt.placeShot(x,y):


#ShipAi.randomGrid()
#print(ShipAi.randomGrid())
#ShipAi.gridToStr(ShipAi.randomGrid())

#print(Ship().parseSaveData('Letadlová loď,default,5,1,11111'))

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
