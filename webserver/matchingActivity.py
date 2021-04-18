import sqlite3
from flask_login import UserMixin

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
def getPositionT(arg1, arg2, arg3, arg4, query):
    try:
        conn = sqlite3.connect('leaguemate.db')
        conn.row_factory = dict_factory
        c = conn.cursor()
        if arg4 == 'AnyType':
            query = "SELECT U.Username, L.QueueType, L.LeagueID, U.GoodAtPosition, U.GoodAtRole, U.GoodAtChamp FROM UserGoodAt U, LeagueAccount L, UserLeague A WHERE U.Username = A.Username AND A.LeagueID = L.LeagueID AND U.GoodAtPosition=(?) AND L.AccountRank BETWEEN (?) AND (?)" 
            c.execute(query, (arg1,arg2,arg3),)
        else:
            c.execute(query, (arg1,arg2,arg3,arg4),)
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

def getMatch(arg1, arg2, arg3, arg4):
    arg2 = switch(arg2)
    arg3 = switch(arg3)
    que = "SELECT U.Username, L.QueueType, L.LeagueID, U.GoodAtPosition, U.GoodAtRole, U.GoodAtChamp FROM UserGoodAt U, LeagueAccount L, UserLeague A WHERE U.Username = A.Username AND A.LeagueID = L.LeagueID AND U.GoodAtPosition=(?) AND L.AccountRank BETWEEN (?) AND (?) AND  L.QueueType =(?) " 
    return getPositionT(arg1, arg2, arg3, arg4, que)

def updatePreferMatch(arg1, arg2, arg3, arg4):
    que = "SELECT U.userName, L.gameRole, R.accountRange, L.champion FROM LeagueAccount L, LeagueAccountRank, UserAccountU, PreferMatch P GROUP BY P.userID=(?) AND U.userID=P.userID"
    return getPositionT(arg1, arg2, arg3, arg4, que)

def switch(argument):
    switcher = {
        'N/A': 0,
        'Iron': 1,
        'Bronze': 2,
        'Silver': 3,
        'Gold': 4,
        'Platinum': 5,
        'Diamond': 6,
        'Master': 7,
        'Grandmaster': 8,
        'Challenger': 9
    }
    print('switcher:')
    print(switcher.get(argument), 'nothing')
    return switcher.get(argument, "nothing")
    

