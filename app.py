from flask import Flask, render_template, url_for, request, session, redirect
from flask_bcrypt import Bcrypt
from flask import flash

from events.event import Event
from events.event_dao import EventDao
from reservations.reservation import Reservation
from reservations.reservation_dao import ReservationDao
from users.user import User
from users.user_dao import UserDao
from paiements.paiement import Paiement
from paiements.paiement_dao import PaiementDao

app = Flask(__name__)
app.secret_key='secretkey'
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    message=None
    user=None
    req = request.form
    if request.method == "POST":
        nom_complet = req['nom_complet']
        username = req['username']
        password = req['password']
        email = req['email']
        status = req['status']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        if nom_complet=="" or username=="" or password=="" or email=="" or status=="":
            message="error"
        else:
                
            user = User(nom_complet,username,hashed_password,email,status)
            message = UserDao.create(user)
    return render_template('user/register.html', message=message,user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    req= request.form
    message = None
    user = None
    if request.method == "POST":
        username = req['username']
        password = req['password']
        if username == '' or password == '':
            message = 'error'
        else:
            (message,user) =  UserDao.get_one(username,password)
            if message=='Success' and user != None:
                if bcrypt.check_password_hash(user[3], password):
                    session['username'] = user[2]
                    session['nom_complet'] = user[1]
                    session['status'] = user[5]
                    session['user'] = user
                    return redirect(url_for('home'))
                else:
                    message = 'Nom d\'user ou mot de passe incorrect.'
            else:
                message = 'Nom d\'user ou mot de passe incorrect.'
        print(message)
            
    return render_template("user/login.html",message=message,user=user)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('user/login'))

@app.route("/player")
def player():
    return render_template("player.html")

@app.route("/events")
def events():
    events = EventDao.lister_evenements()
    return render_template("events.html", events=events)

@app.route("/admin/events", methods=['GET', 'POST'])
def admin_events():
    if request.method == 'POST':
        action = request.form.get('action')
        event_id = request.form.get('event_id')

        if action == 'add':
            
            nom = request.form['nom']
            date = request.form['date']
            emplacement = request.form['emplacement']
            prix = request.form['prix']
            EventDao.ajouter_evenement(Event(nom, date, emplacement, prix))
            pass
        elif action == 'edit':
            
            nom = request.form['nom']
            date = request.form['date']
            emplacement = request.form['emplacement']
            prix = request.form['prix']
            event_id = request.form['event_id']
            evt = Event(nom, date, emplacement, prix)
            EventDao.modifier_evenement(event_id, evt)
            pass
        elif action == 'cancel':
            
            event_id = request.form['event_id']
            EventDao.supprimer_evenement(event_id)
            pass
        return redirect(url_for('admin_events'))

    events = EventDao.lister_evenements()
    return render_template('admin/event_admin.html', events=events)

@app.route("/admin/users", methods=['GET', 'POST'])
def admin_users():
    action = request.form.get('action')
    user_id = request.form.get('user_id')
    if request.method == 'POST':
        
        if action == 'add':
            nom_complet = request.form['nom_complet']
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            status = request.form['status']
            usr = User(nom_complet, username, password, email, status)
            UserDao.create(usr)

        elif action == 'edit':
            new_status = request.form.get('status')
            if user_id and new_status:
                UserDao.edit_user_status(user_id , new_status)
                return redirect(url_for('admin_users'))
            else:
                return "error"
            

        elif action == 'delete':
            user_id = request.form['user_id']
            UserDao.delete_user(user_id)

    users = UserDao.list_all()
    return render_template('admin/user_admin.html', users=users)

@app.route('/admin/reservations', methods=['GET', 'POST'])
def admin_reservations():
    if request.method == 'POST':
        action = request.form.get('action')
        reservation_id = request.form.get('reservation_id', type=int)

        if action == 'update_status':
            new_status = request.form.get('status')
            message = ReservationDao.annuler_reservation(new_status, reservation_id)
            flash(message)
            return redirect(url_for('admin_reservations'))
        elif action == 'delete':
            message = ReservationDao.supprimer_reservation(reservation_id)
            flash(message)
    
    # Afficher toutes les réservations
    reservations, message_reservations = ReservationDao.afficher_places_reservees()
    if message_reservations != "Success":
        flash(message_reservations)  
    
    # Calculer les places disponibles
    message_disponibles, places_disponibles = ReservationDao.nombre_places_disponibles()
    if message_disponibles != "Success":
        flash(message_disponibles)
    
    return render_template('admin/reservations_admin.html', reservations=reservations, places_disponibles=places_disponibles)

@app.route("/profil")
def profil():
    user = session['user']
    nom_complet = user[1]
    
    message, reservations = ReservationDao.filtrer_reservations_par_personne(nom_complet)
    print("reservations",reservations)
    if 'username' in session:
        username = session['username']
        if user:
            nom_complet = user[1]  
            
            print(message,reservations)
            if message == "Success":
                return render_template('user/profil.html',message=message, user=user, reservations=reservations)
            else:
                return "Erreur lors de la récupération des réservations", 500
        else:
            return "Profil non trouvé", 404
    return redirect(url_for('login'))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/reservation', methods=['GET', 'POST'])
def creer_reservation():
    events = EventDao.lister_evenements()
    message_disponibles, places_disponibles = ReservationDao.nombre_places_disponibles()
    if message_disponibles != "Success":
        flash(message_disponibles)
    
    if request.method == 'POST':
        nom = request.form['nom']
        place = request.form['place']
        status = request.form['status']
        event = request.form['event']
        nouvelle_reservation = Reservation(nom, place, status, event)
        message = ReservationDao.reserver_place(nouvelle_reservation)

        if "Success" in message:
            return redirect(url_for('afficher_reservations'))
        else:
            return render_template('reservation/reservation.html', message=message)
    else:
        return render_template('reservation/reservation.html', events=events, places_disponibles=places_disponibles)

@app.route('/reservations')
def afficher_reservations():
    reservations, message = ReservationDao.afficher_places_reservees()
    return render_template('reservation/liste_reservations.html',reservations=reservations, message=message)

@app.route('/paiement', methods=['POST','GET'])
def soumission_paiement():
    paiement=None
    message = None
    if request.method == "POST":
   
        nom_complet = request.form['nom_complet']
        telephone = request.form['telephone']
        email = request.form['email']
        carte_credit = request.form['carte_credit']
        pmts= Paiement(nom_complet,telephone,email,carte_credit)
        message = PaiementDao.add_payment(pmts)
        if "Success" in message:
            return redirect(url_for('merci'))
        
    return render_template("paiement/paiement.html", paiement=paiement)

@app.route('/merci')
def merci():
    return render_template("paiement/merci.html")