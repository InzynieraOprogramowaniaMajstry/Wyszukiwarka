import sys
import os

from initialize_objects import csrf
from models.database_operations import DatabaseOperations

from flask import Blueprint, request, flash, make_response, render_template, redirect, url_for

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")

user_bp = Blueprint('user_bp', __name__)

LIBRARY = "library.html"

@user_bp.route("/")
def index():
    """Return main page"""
    user_id = request.cookies.get('user_id')
    return render_template("main.html", user_id=user_id)


@user_bp.route("/login")
def login():
    """Return login page"""
    user_id = request.cookies.get('user_id')
    return render_template("login.html", user_id=user_id)


@user_bp.route("/register")
def register():
    """Return register page"""
    user_id = request.cookies.get('user_id')
    return render_template("register.html", user_id=user_id)


@user_bp.route("/logout")
def logout_user():
    """Clear user cookies and return main page"""
    flash("You have been logged out")
    resp = make_response(render_template("main.html"))
    resp.set_cookie('email', '', expires=0, secure=True)
    resp.set_cookie('user_id', '', expires=0, secure=True)
    return resp


@user_bp.route("/library")
def profile():
    """Read user cookies and return library"""
    email = request.cookies.get('email')
    user_id = request.cookies.get('user_id')
    if user_id is None:
        flash("You are not logged in!")
        return redirect(url_for('user_bp.index'))
    else:
        return render_template(LIBRARY, email=email, user_id=user_id)


@user_bp.route("/library", methods=['POST'])
def login_user():
    """Check if filled email and password matches saved in the database and if so, set user cookies and return its
    library page"""
    email = request.form['login']
    password = request.form['password']
    if DatabaseOperations.check_if_password_matches(email, password):
        user_id = DatabaseOperations.get_user_id(email)
        resp = make_response(render_template(LIBRARY, email=email, user_id=user_id))
        resp.set_cookie('email', value=email, secure=True)
        resp.set_cookie('user_id', value=str(user_id), secure=True)
        return resp
    else:
        flash('Wrong login or password')
        return redirect(url_for('user_bp.login'))


@user_bp.route("/login", methods=['POST'])
def add_user():
    """Check if user with given email doesn't exist and if not, add new user to the database, set user cookies
     and return its library page."""
    email = request.form['login']
    password = request.form['password']
    if DatabaseOperations.check_if_email_exists(email):
        flash('User with given email already exists')
        print("exists user")
        return redirect(url_for('user_bp.register'))
    else:
        print("create new user")
        user_id = DatabaseOperations.add_user(email, password)
        resp = make_response(render_template(LIBRARY, email=email, user_id=user_id))
        resp.set_cookie('email', value=email, secure=True)
        resp.set_cookie('user_id', value=str(user_id), secure=True)
        return resp
