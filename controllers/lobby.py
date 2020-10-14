from conf import db

def create(req):
    name = req.json['name'];
    print('Přidat:  ' + name);
    cur = db.cursor()
    cur.execute('INSERT INTO lobbies (name) VALUES (?)',(name))
    db.commit()
    return '',201
