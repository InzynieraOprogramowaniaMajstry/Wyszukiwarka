import sys
import os
from models.wolne_lektury_api import WolneLekturyAPI
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")

from models.database import db, User

from flask import Blueprint ,request, flash
user_bp = Blueprint('user_bp', __name__)

from flask import json, render_template, redirect, url_for

@user_bp.route("/")
def index():
    return render_template("base.html")

@user_bp.route("/login")
def login():
    return render_template("login.html")

@user_bp.route("/register")
def register():
    return render_template("register.html")


@user_bp.route("/api")
def a():
    return WolneLekturyAPI.books_list

@user_bp.route("/kinds")
def b():
    return WolneLekturyAPI.kinds_list

@user_bp.route("/authors")
def simple_query():
    return WolneLekturyAPI.authors_list 

@user_bp.route("/user")
def user():
    return render_template("user.html")


@user_bp.route("/profile",methods=['GET','POST'])
def go_to_profile():
    email = request.form['login']
    password = request.form['password']
    print(email)
    print(password)
    query = db.session.query(User).filter(User.email==email, User.password==password)
    if query.first():
        return render_template("profile.html", email=email)
    else:
        flash('Wrong login or password')
        return redirect(url_for('user_bp.login'))

@user_bp.route("/login",methods=['GET','POST'])
def add_user():
    email = request.form['login']
    password = request.form['password']
    query = db.session.query(User).filter(User.email==email)
    print(email)
    print(password)
    if query.first():
        flash('User with given email already exists')
        print("exists user")
        return redirect(url_for('user_bp.register'))
    else:
        print("create new user")
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_bp.login'))



    