import mysql.connector as mysql

def connexion_db():
    return mysql.connect(
        user='root',
        password= 'Bingo12345',
        host='localhost',
        database='projet_session'
        )
