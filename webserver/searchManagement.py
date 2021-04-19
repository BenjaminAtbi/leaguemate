import sqlite3
from flask_login import UserMixin

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
def getUserDataL(arg1, arg2, arg3, query):
    try:
        conn = sqlite3.connect('leaguemate.db')
        conn.row_factory = dict_factory
        c = conn.cursor()
        if (arg3 and arg2 and arg3) == 'Any':
            query = getAllUsers()
            c.execute(query)
        elif arg3 == 'max':
            c.execute(query)
        elif arg3 == 'lane':
            c.execute(query, (arg1),)
        else:
            c.execute(query, (arg1, arg2, arg3),)
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

def getAllUsers():
    que = "select * from UserLeague as C left outer join LeagueAccount as L on L.LeagueID = C.LeagueID left outer join UserAccount as U on C.Username = U.Username" 
    return que

def getMaxLevel(arg1, arg2, arg3):
    que = " select Username,GameServer,LeagueID,GameLevel from (select GameServer, LeagueID as MaxLevelID, Gamelevel from leagueaccount where GameLevel = (select max(GameLevel) from leagueaccount)) R1 join (select Username,LeagueID  from userleague)R2  on R1.MAXLevelID = R2.LeagueID"
    return getUserDataL(arg1, arg2, 'max', que)

def countGoodAtChamp():
    que ="select GoodAtChamp, count(*) from usergoodat group by GoodAtChamp"
    return que

def sortUsers(arg1, arg2, arg3):
    arg2 = switch(arg2)
    que ="select * from UserLeague as C left outer join LeagueAccount as L on L.LeagueID = C.LeagueID left outer join UserAccount as U on C.Username = U.Username WHERE L.Position = (?) AND L.AccountRank = (?) AND l.QueueType =(?) ORDER BY L.GameLevel desc"
    return getUserDataL(arg1, arg2, arg3, que)

def searchLane(arg1):
    
    que ="select GameServer, LeagueID, GameLevel, AccountRank, QueueType, TFTRank from leagueaccount L1 where exists (select LeagueID, GameServer from (select leagueID, GameServer from userleague U1 where exists (select Username from usergoodat where U1.Username = usergoodat.Username and usergoodat.GoodAtPosition <> (?)))R1 where R1.LeagueID = L1.LeagueID)"
    return getUserDataL(arg1, 0, 'lane', que)


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
    

