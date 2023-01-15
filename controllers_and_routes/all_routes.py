import sys
import os
from models.wolne_lektury_api import WolneLekturyAPI

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")

from models.database import db, User
from models.database_operations import DatabaseOperations

from flask import Blueprint, request, flash, make_response

user_bp = Blueprint('user_bp', __name__)

from flask import json, render_template, redirect, url_for


@user_bp.route("/")
def index():
    return render_template("main.html")


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


@user_bp.route("/profile")
def profile():
    email = request.cookies.get('email')
    user_id = request.cookies.get('user_id')
    return render_template("profile.html", email=email, user_id=user_id)


@user_bp.route("/profile", methods=['GET', 'POST'])
def login_user():
    email = request.form['login']
    password = request.form['password']
    # print(email)
    # print(password)
    # query = db.session.query(User).filter(User.email==email, User.password==password)
    if DatabaseOperations.check_if_password_matches(email, password):
        user_id = DatabaseOperations.get_user_id(email)
        resp = make_response(render_template("profile.html"))
        resp.set_cookie('email', value=email)
        resp.set_cookie('user_id', value=str(user_id))
        return resp
    else:
        flash('Wrong login or password')
        return redirect(url_for('user_bp.login'))


@user_bp.route("/login", methods=['GET', 'POST'])
def add_user():
    email = request.form['login']
    password = request.form['password']
    #
    # query = db.session.query(User).filter(User.email==email)
    # print(email)
    # print(password)
    if DatabaseOperations.check_if_email_exists(email):
        flash('User with given email already exists')
        print("exists user")
        return redirect(url_for('user_bp.register'))
    else:
        print("create new user")

        user_id = DatabaseOperations.add_user(email, password)
        resp = make_response(render_template("profile.html"))
        resp.set_cookie('email', value=email)
        resp.set_cookie('user_id', value=user_id)
        return resp
