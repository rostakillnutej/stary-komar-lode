from lode import DB

class User(DB.Model):
    __tablename__ = 'uzivatele'
    id = DB.Column(DB.Integer, primary_key=True)
    token = DB.Column(DB.String)
    currentTable = DB.Column(DB.Text)
    dif = DB.Column(DB.Integer)

DB.create_all()
