import database as db
from events.event import Event

class EventDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def ajouter_evenement(cls, evt:Event):
        sql = "INSERT INTO events (nom, date, emplacement, prix) VALUES (%s, %s, %s, %s)"
        params = (evt.nom, evt.date, evt.emplacement, evt.prix)
        try:
            EventDao.connexion.cursor()
            EventDao.cursor.execute(sql, params)
            EventDao.connexion.commit()
            message = "Success"
        except Exception as ex:
            EventDao.connexion.rollback()
            message = "Error"
        return message

    @classmethod
    def lister_evenements(cls):
        sql = "SELECT * FROM events"
        try:
            EventDao.connexion.cursor()
            EventDao.cursor.execute(sql)
            evenements = EventDao.cursor.fetchall()
            message = "Success"
        except Exception as ex:
            return [], "Error"
        return message, evenements
        

    @classmethod
    def modifier_evenement(cls, event_id, evt: Event):
        sql = "UPDATE events SET nom=%s, date=%s, emplacement=%s, prix=%s WHERE id=%s"
        params = (evt.nom, evt.date, evt.emplacement, evt.prix, event_id)
        try:
            EventDao.connexion.cursor()
            EventDao.cursor.execute(sql, params)
            EventDao.connexion.commit()
            message =  "Success"
        except Exception as ex:
            EventDao.connexion.rollback()
            message =  "Error"
        return message
        

    @classmethod
    def supprimer_evenement(cls, event_id):
        sql = "DELETE FROM events WHERE id = %s"
        
        try:
            EventDao.connexion.cursor()
            EventDao.cursor.execute(sql, (event_id,))
            EventDao.connexion.commit()
            message = "Success"
        except Exception as ex:
            EventDao.connexion.rollback()
            message =  "Error"
        return message
        