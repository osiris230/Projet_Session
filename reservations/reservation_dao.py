import database as db
#from reservations.reservation import Reservation
from reservation import Reservation

class ReservationDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def reserver_place(cls, rsv:Reservation): 
            sql = "INSERT INTO reservations (nom, place, status) VALUES (%s, %s, %s)"
            params = (rsv.nom, rsv.place, rsv.status)
            try:
                ReservationDao.connexion.cursor()
                ReservationDao.cursor.execute(sql, params)
                ReservationDao.connexion.commit()
                message = "Success"
            except Exception as ex:
                message = "Error"
            return message
    
    @classmethod
    def afficher_places_reservees(cls):
        sql = "SELECT place FROM reservations"
        try:
            ReservationDao.cursor.execute(sql)
            reservations = ReservationDao.cursor.fetchall()
            ReservationDao.cursor.close()
            message = "Success"
        except Exception as ex:
            message = f"Erreur lors de la récupération des réservations: {ex}"
        return  message, reservations
    
    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale = 200
        sql = "SELECT COUNT(*) FROM reservations"
        try:
            ReservationDao.cursor.execute(sql)
            (nombre_reservations,) = ReservationDao.cursor.fetchone()
            places_disponibles = capacite_totale - nombre_reservations
            message = "Success", places_disponibles
        except Exception as ex:
            message = "Error"
        return message
    
    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = "SELECT * FROM reservations WHERE nom = %s"
        try:
            ReservationDao.connexion.cursor()
            ReservationDao.cursor.execute(sql, (nom,))
            reservations = ReservationDao.cursor.fetchall()
            message = "Success"
        except Exception as ex:
            message = "Error"
        return  message, reservations
    
    @classmethod
    def annuler_reservation(cls, nom):
        sql = "DELETE FROM reservations WHERE nom = %s"
        try:
            ReservationDao.connexion.cursor()
            ReservationDao.cursor.execute(sql, (nom,))
            ReservationDao.connexion.commit()
            
            message = f"Toutes les réservations pour {nom} ont été annulées."
        except Exception as ex:
            print(f"Erreur lors de l'annulation des réservations pour {nom}: {ex}")
        return message