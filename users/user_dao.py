import database as db
import flask_bcrypt as bcrypt
from users.user import User

#from user import User
# init ^


class UserDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, usr:User):
       
        sql = "INSERT INTO users (nom_complet, username, password, email, status) VALUES (%s, %s, %s, %s, %s)"
        params = (usr.nom_complet, usr.username, usr.password,usr.email,usr.status)
        try:
            UserDao.cursor.execute(sql,params)
            UserDao.connexion.commit()
            message = "Success"
        except Exception as exc:
            message = "Error"
        return message
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM users"
        UserDao.cursor.execute(sql)
        user = UserDao.cursor.fetchall()
        
        return user
    
    @classmethod
    def get_one(cls,username,password):
        sql = "SELECT * FROM users WHERE username=%s"
        try:
            UserDao.cursor.execute(sql, (username,))
            user = UserDao.cursor.fetchone()
            if user:
                if bcrypt.check_password_hash(user[3], password):
                    message = "Success"
        except Exception as ex:
            message = "Error"
            user = []
        return (message,user)
    
    @classmethod
    def get_by_username(cls, username):
        sql = "SELECT * FROM users WHERE username = %s"
        try:
            UserDao.cursor.execute(sql, (username,))
            user = UserDao.cursor.fetchone()
            message = "Success"
        except Exception as ex:
            message = "Error"
            user = []
        return (message, user)