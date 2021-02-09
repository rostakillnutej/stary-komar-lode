import json,uuid
from flask import request, send_from_directory, make_response
from flask_socketio import send, emit
from lode import app, socketio, DB
from lode.models.InstanceManager import InstanceManager

from lode.db.userModel import User





#Statický obsah

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')
    pass


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
imp = InstanceManager('plan')
#Všechny cesty které manipulují s planovacímí instancemi
@socketio.on('connect', namespace='/plan')
def conPlan():
    imp.add(request.sid,isUser(request))
@socketio.on('disconnect', namespace='/plan')
def disconPlan():
    imp.delete(request.sid)
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
def fnish(dif):

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
    data.dif = dif
    DB.session.commit()
    imp.delete(request.sid)
    emit('finishStatus',True, namespace='/plan')



#Správce hracích instancí
img = InstanceManager('game')

#Všechny cesty které manipulují s hracímí instancemi
@socketio.on('connect', namespace='/game')
def conGame():


    data = isUser(request)


    # Z totoho vybrat obtížnost

    if not(data) or data.currentTable == '':
        emit('userError',False, namespace='/game')
        return

    img.add(request.sid,data)
    payload = img.getIns(request.sid).returnData
    emit('returnTable',payload, namespace='/game')

    if img.getIns(request.sid).changed:
        x = ins.changed[0][0]
        y = ins.changed[0][1]
        val = ins.changed[1]
        emit('myTableUpdate','{}#{}#{}'.format(x,y,val), namespace='/game')



@socketio.on('disconnect', namespace='/game')
def disconGame():
    img.delete(request.sid)
    #print(imp.ins)

@socketio.on('hit', namespace='/game')
def hitEvent(pos):
    ins = img.getIns(request.sid)
    if not(ins):
        return False
    #PŘIDAT VALIDACI VSTUPU BY BYLO DOBRÉ
    data = pos.split('#')
    result = ins.handleHit(int(data[0]),int(data[1]))
    if result[0]:
        emit('eTableUpdate',pos + '#' + str(result[1]), namespace='/game')
        #emit('mTableUpdate', , namespace='/game')

    if ins.changed:
        x = ins.changed[0][0]
        y = ins.changed[0][1]
        val = ins.changed[1]
        emit('myTableUpdate','{}#{}#{}'.format(x,y,val), namespace='/game')

    if ins.winner:
        emit('endGame', ins.winner, namespace='/game')






#@socketio.on('my broadcast event', namespace='/test')
#def test_message(message):
#    emit('my response', {'data': message['data']}, broadcast=True)
