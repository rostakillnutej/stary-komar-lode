from flask import jsonify
from flask_socketio import send, emit
import uuid

def establish():
    token = str(uuid.uuid4())
    usersUids.append(token)
    eventData = {
        'uid': token
    }
    emit('establish', eventData)
    #print(usersUids)
