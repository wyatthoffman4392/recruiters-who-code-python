import sqlite3
connection = sqlite3.connect('example.db')

cur = connection.cursor()

for row in cur.execute('SELECT * FROM Bikes'):
    print(row)