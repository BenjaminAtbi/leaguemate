from flask_login import UserMixin
import sqlite3

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
class User(UserMixin):
    id = None
    password = None
    name = None 

def getUser(arg, query):
    conn = sqlite3.connect('leaguemate.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(query, (arg,))
    userdata = c.fetchall()
    if(userdata):
        user = User()
        user.id = userdata[0]['AccountName']
        user.password = userdata[0]['AccountPassword']
        user.name = userdata[0]['Username']
        return user
    else:
        return None

def getUserData(arg, fields):
    conn = sqlite3.connect('leaguemate.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(query, (arg,))
    userdata = c.fetchall()


def getUserbyID(id):
    return getUser(id, "SELECT * from UserAccount where AccountName=(?)")

def getUserbyName(username):
    return getUser(username, "SELECT * from UserAccount where Username=(?)")
