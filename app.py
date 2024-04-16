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
                
            user = user(nom_complet,username,hashed_password,email,status)
            message = UserDao.create(user)
    return render_template(f'register.html', message=message,user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    req= request.form
    message = None
    user = None
    if request.method == "POST":
        username = req['username']
        password = req['mdp']
        if username == '' or password == '':
            message = 'error'
        else:
            (message,user) =  UserDao.get_one(username,password)
            if message=='Success' and user != None:
                if bcrypt.check_password_hash(user[3], password):
                    session['username'] = user[2]
                    session['nom'] = user[1]
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