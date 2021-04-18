import sqlite3
import os

filepath = 'Newdatabase.sql'
dbpath = 'leaguemate.db'

try:
    os.remove(dbpath)
except:
    print("db didn't exist/failed to remove old version")

f = open(filepath)
query = f.read()
query = query.split(';')
conn = sqlite3.connect(dbpath)
c = conn.cursor()
for statement in query:
    
    try:
        c.execute(statement)
    except sqlite3.Error as e:
        print("error: ",e.args[0])
        print("statement: ",statement)
conn.commit()
print("loaded db")
