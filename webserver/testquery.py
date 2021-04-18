import sqlite3
import sys

dbpath = 'leaguemate.db'

query = sys.argv[1]
conn = sqlite3.connect(dbpath)
c = conn.cursor()

print(query)
# try:
c.execute(query)
# except sqlite3.Error as e:
#     print("error: ", e.args[0])

print(c.fetchall())
for row in c.fetchall():
    print(row)