from flask import jsonify
from db import newDb

def create(req):
    name = req.json['name'];
    db = newDb()
    cur = db.cursor()
    cur.execute("INSERT INTO lobbies (name) VALUES (?)",(name,))
    db.commit()
    return '',201

def get(req):
    cur = newDb().cursor()
    cur.execute("SELECT * FROM lobbies")
    rows = cur.fetchall()
    return jsonify(rows),201
