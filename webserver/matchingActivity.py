import sqlite3
import pandas as pd
from flask_login import UserMixin


#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
class User(UserMixin):
    id = None
    gameLevel = None
    champion = None
    gameRole = None
    TFTrank = None
    matchedLeagueid = None

def getPositionT(arg, query):
    conn = sqlite3.connect('leaguemate.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    #query and print table with chosen Position
    c.execute(query, (arg,))
    positiondata = c.fetchall()
    if(positiondata):
        user = User()
        user.matchedLeagueid = positiondata[0]['leagueID']
        user.gameLevel = positiondata[0]['gameLevel']
        user.champion = positiondata[0]['champion']
        user.gameRole = positiondata[0]['gameRole']
        user.TFTrank = positiondata[0]['TFTrank']
        return user
    else:
        return None

    return positiondata

def getPositionbyInp(id):
    return getPositionT(id, "SELECT * from LeagueAccount WHERE gameRole=(?)")


    

