import sqlite3
from flask_login import UserMixin

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
def getPositionT(arg1, arg2, query):
    try:
        conn = sqlite3.connect('leaguemate.db')
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(query, (arg1,arg2),)
        result = c.fetchall()
        for row in result:
           print(row)
        return result
    except sqlite3.Error as error:
        print("failed to read from table", error)
    finally:
        if conn:
            conn.close()
            print("the sqlite connection is closed")

def getPositionbyInp(arg1, arg2):
    que = "SELECT U.userName, U.leagueID, L.gameRole FROM UserAccount U, LeagueAccount L, LeagueAccountRank R WHERE U.leagueID = L.leagueID AND R.leagueID = L.leagueID AND L.gameRole=(?) AND L.champion=(?)"
#    que = "SELECT * from LeagueAccount WHERE gameRole=(?)"

    return getPositionT(arg1, arg2, que)

def getMatchedUserInfo(arg1, arg2):
    que = "SELECT U.userName, L.gameRole, R.accountRange, L.champion FROM LeagueAccount L, LeagueAccountRank, UserAccountU, PreferMatch P GROUP BY P.userID=(?) AND U.userID=P.userID"
    return getPositionT(arg1, arg2, que)



    

