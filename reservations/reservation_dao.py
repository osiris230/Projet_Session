import database as db
from reservations.reservation import Reservation
#from reservation import Reservation
# init ^

class ReservationDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def reserver_place(cls, rsv:Reservation): 
            sql = "INSERT INTO reservations (nom, place, status, event) VALUES (%s, %s, %s, %s)"
            params = (rsv.nom, rsv.place, rsv.status, rsv.event)
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
        sql = "SELECT * FROM reservations"
        try:
            ReservationDao.cursor.execute(sql)
            reservations = ReservationDao.cursor.fetchall()
            message = "Success"
        except Exception as ex:
            reservations = []
            message = f"Erreur lors de la récupération des réservations: {ex}"
        return  reservations, message
    
    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale = 10000
        sql = "SELECT COUNT(*) FROM reservations"
        try:
            ReservationDao.cursor.execute(sql)
            (nombre_reservations,) = ReservationDao.cursor.fetchone()
            places_disponibles = capacite_totale - nombre_reservations
            message = "Success"
        except Exception as ex:
            message = "Error"
        return message , places_disponibles
    
    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = "SELECT * FROM reservations WHERE nom = %s"
        reservations = None
        try:
            ReservationDao.connexion.cursor()
            ReservationDao.cursor.execute(sql, (nom,))
            reservations = ReservationDao.cursor.fetchall()
            message = "Success"
        except Exception as ex:
            print(ex)
            message = "Error"
        return  message, reservations
    
    @classmethod
    def annuler_reservation(cls,new_status, rsv_id):
        sql = "UPDATE reservations SET status=%s WHERE id=%s"
        params = (new_status, rsv_id)
        try:
            cls.connexion.cursor()
            cls.cursor.execute(sql, params)
            cls.connexion.commit()
            return "Statut mis à jour avec succès"
        except Exception as ex:
            return f"Erreur lors de la mise à jour du statut: {ex}"
    
    @classmethod
    def find_by_id(cls, reservation_id):
        sql = "SELECT * FROM reservations WHERE id = %s"
        try:
            ReservationDao.cursor.execute(sql, (reservation_id,))
            reservation = ReservationDao.cursor.fetchone()
            return reservation 
        except Exception as ex:
            print(f"Erreur lors de la recherche de la réservation: {ex}")
            return None
        
    @classmethod
    def supprimer_reservation(cls, rsv_id):
        sql = "DELETE FROM reservations WHERE id=%s"
        try:
            cls.cursor.execute(sql, (rsv_id,))
            cls.connexion.commit()
            return "Réservation supprimée avec succès"
        except Exception as ex:
            return f"Erreur lors de la suppression de la réservation: {ex}"