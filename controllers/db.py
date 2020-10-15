import sqlite3
def newDb():
    return sqlite3.connect('data/main.db')
