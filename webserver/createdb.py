import sqlite3

conn = sqlite3.connect('leaguemate.db')

c = conn.cursor()

sql_file=open('database.sql')
sql_as_str=sql_file.read()
c.executescript(sql_as_str)
