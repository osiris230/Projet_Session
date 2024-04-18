from flask import Flask, render_template, url_for, request, session, redirect
from flask_bcrypt import Bcrypt

from events.event import Event
from events.event_dao import EventDao
from reservations.reservation import Reservation
from reservations.reservation_dao import ReservationDao
from users.user import User
from users.user_dao import UserDao

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
    return render_template('register.html', message=message,user=user)

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
                    session['user'] = user
                    return redirect(url_for('home'))
                else:
                    message = 'Nom d\'user ou mot de passe incorrect.'
            else:
                message = 'Nom d\'user ou mot de passe incorrect.'
        print(message)
            
    return render_template("login.html",message=message,user=user)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/player")
def player():
    return render_template("player.html")

@app.route("/events")
def events():
    events = EventDao.lister_evenements()
    return render_template("events.html", events=events)

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
                return render_template('profil.html',message=message, user=user, reservations=reservations)
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
            return render_template('reservation.html', message=message)
    else:
        # Affiche le formulaire de création de la réservation
        return render_template('reservation.html')

@app.route('/reservations')
def afficher_reservations():
    reservations, message = ReservationDao.afficher_places_reservees()
    return render_template('liste_reservations.html',reservations=reservations, message=message)


