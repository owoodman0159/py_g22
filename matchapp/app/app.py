import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.profile import *

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/matchapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'a_default_secret_key')

db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/profile/<int:uid>')
def profile(uid):
    user_info = get_user_info(uid)

    if user_info != ():
        return render_template("profile.html", user=user_info)
    else:
        return render_template("index.html")



@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    location = request.form['location']
    age = request.form['age']
    
    userid = add_user(name, email, gender, location, age)  
    
    if userid > 0:
        flash(f"User created successfully with Userid{userid}")
        return redirect(url_for('profile', uid=userid))
        
    else:
        flash("Failed to create user")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)