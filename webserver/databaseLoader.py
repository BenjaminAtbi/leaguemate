import sqlite3
import os

filepath = 'Newdatabase.sql'
dbpath = 'leaguemate.db'

os.remove(dbpath)
f = open(filepath)
query = f.read()
query = query.split(';')
for statement in query:
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(statement)