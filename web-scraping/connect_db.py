import sqlite3
from sqlite3 import Error

def connect_db(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection Successful!')
    except Error as e:
        print(f'ERROR: {e}')
    
    return connection

connect_db('web-scraping/example.db')

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE Bikes (BikeID real, Name varchar(255), Price real)''')

cursor.execute(
    '''INSERT INTO Bikes VALUES (1, 'Trek Marlin', 100)''')

connection.commit()
connection.close()
