import json,uuid
from flask import request, send_from_directory, make_response
from flask_socketio import send, emit
from lode import app, socketio, DB
from lode.models.InstanceManager import InstanceManager

from lode.db.userModel import User

#Statický obsah
'''
@app.route('/', methods=['GET'])
def index():
    #return app.send_static_file('index.html')
    pass
'''

#Funkce na vybŕaní uživatele z databáze
def isUser(request):
    token = request.cookies.get('user')
    #Když uživatel ještě nemá cookies
    if(not(token)):
        return False
    #Hledání v uživatele v databazi
    data = DB.session.query(User).filter_by(token=token).first()
    DB.session.commit()
    #Když je uživatel nalezen tak ho vrátí
    if data:
        return data
    return False

#Hledá existenci uživatele při načtení stránky
@app.route('/user', methods=['GET'])
def user():
    data = isUser(request)
    if not(data):
        token = str(uuid.uuid4())
        newUser = User(token=token,currentTable='')
        DB.session.add(newUser)
        DB.session.commit()
        res = make_response()
        res.set_cookie('user', token, max_age=60*60*24*365*2)
        return res,201
    else:
        return 'Účet už existuje',201


#Správce plánovacích instancí
imp = InstanceManager()
#Všechny cesty které manipulují s planovacímí instancemi
@socketio.on('connect', namespace='/plan')
def conPlan():
    imp.add(request.sid,isUser(request))
    print(imp.ins)
@socketio.on('disconnect', namespace='/plan')
def disconPlan():
    imp.delete(request.sid)
    print(imp.ins)
@socketio.on('getShips', namespace='/plan')
def getShips():
    ins = imp.getIns(request.sid)
    if not(ins):
        return
    emit('returnShips', json.dumps(ins.getDocks()), namespace='/plan')
@socketio.on('getDraftTable', namespace='/plan')
def getTable():
    ins = imp.getIns(request.sid)
    if not(ins):
        return
    emit('returnDraftTable', ins.table.getSaveData(), namespace='/plan')
@socketio.on('rotateShip', namespace='/plan')
def rotate(data):
    ins = imp.getIns(request.sid)
    if not(ins):
        return
    ins.handleShipRotate(data)
    emit('returnShips', json.dumps(ins.getDocks()), namespace='/plan')
@socketio.on('placeShip', namespace='/plan')
def place(id,x,y):
    ins = imp.getIns(request.sid)
    if not(ins):
        return
    emit('placeStatus', json.dumps(ins.handlePlace(id,x,y)), namespace='/plan')
@socketio.on('removeShip', namespace='/plan')
def remove(id):
    ins = imp.getIns(request.sid)
    if not(ins):
        return
    result = ins.handleRemove(id)
    if(result[0]):
        result[0] = result[0].getSaveData()
        result.append(id)
    emit('removeStatus', json.dumps(result), namespace='/plan')

#Ukončení plánovací instance
@socketio.on('finish', namespace='/plan')
def fnish():
    ins = imp.getIns(request.sid)
    if not(ins):
        return
    #Kontrola položení všech lodí
    if len(ins.dock) > 0:
        emit('finishStatus',False, namespace='/plan')
        return
    #Kontrola uživatele
    data = isUser(request)
    if not(data):
        emit('finishStatus',False, namespace='/plan')
        return
    #Přidání naplánované tabulky do db
    data.currentTable = ins.table.getSaveData()
    DB.session.commit()
    imp.delete(request.sid)
    emit('finishStatus',True, namespace='/plan')







#Správce hracích instancí
#imp = InstanceManager()

#Všechny cesty které manipulují s hracímí instancemi



#@socketio.on('my broadcast event', namespace='/test')
#def test_message(message):
#    emit('my response', {'data': message['data']}, broadcast=True)
