import sqlite3
from flask_login import UserMixin

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
def getUserDataL(query):
    try:
        conn = sqlite3.connect('leaguemate.db')
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(query)
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
    return getUserDataL(que)

def getAllChampions():
    try:
        conn = sqlite3.connect('leaguemate.db')
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute("SELECT GoodAtChamp, count(*) as num FROM usergoodat GROUP BY GoodAtChamp ORDER BY num DESC")
        result = c.fetchall()
        return result
    except sqlite3.Error as error:
        print("failed to read from table", error)
    finally:
        if conn:
            conn.close()
            print("the sqlite connection is closed")

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
    

