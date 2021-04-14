import sqlite3
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
    matched_matchedLeagueid = None
    matched_gameLevel = None
    matched_champion = None
    matched_gameRole = None
    matched_TFTrank = None
    

def getPositionT(arg, query, selfID):
    conn = sqlite3.connect('leaguemate.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(query, (arg,))
    userdata = c.fetchall()
    if(userdata):
        user = User()
        user.id = selfID
        user.matchedLeagueid = userdata[0]['leagueID']
        user.matched_gameLevel = userdata[0]['gameLevel']
        user.matched_champion = userdata[0]['champion']
        user.matched_gameRole = userdata[0]['gameRole']
        user.matched_TFTrank = userdata[0]['TFTrank']
        print(user.matched_champion)
        print(user.matched_matchedLeagueid)
        print(user.matched_gameLevel)
        return user
    else:
        return None

def getPositionbyInp(id, selfID):
    return getPositionT(id, "SELECT * from LeagueAccount WHERE gameRole=(?)", selfID)


    

