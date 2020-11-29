from lode import DB

class User(DB.Model):
    __tablename__ = 'uzivatele'
    id = DB.Column(DB.Integer, primary_key=True)
    token = DB.Column(DB.String)
    currentTable = DB.Column(DB.Text)

DB.create_all()
