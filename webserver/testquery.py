import sqlite3
import sys

dbpath = 'leaguemate.db'

query = sys.argv[1]
conn = sqlite3.connect(dbpath)
c = conn.cursor()
c.execute(query)
print(c.fetchall())