import sys
import os

from initialize_objects import csrf
from models.database_operations import DatabaseOperations

from flask import Blueprint, request, flash, make_response, render_template, redirect, url_for

from models.wolne_lektury_api import WolneLekturyAPI

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")

user_bp = Blueprint('user_bp', __name__)

LIBRARY = "library.html"
NOT_LOGGED = "Nie jesteś zalogowany!"
INDEX = 'user_bp.index'


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
    flash("Zostałeś wylogowany")
    resp = make_response(render_template("main.html"))
    resp.set_cookie('email', '', expires=0, secure=True, httponly=True)
    resp.set_cookie('user_id', '', expires=0, secure=True, httponly=True)
    return resp


@user_bp.route("/library")
def profile():
    """Read user cookies and return library"""
    email = request.cookies.get('email')
    user_id = request.cookies.get('user_id')
    if user_id is None:
        flash(NOT_LOGGED)
        return redirect(url_for(INDEX))
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
        resp.set_cookie('email', value=email, secure=True, httponly=True)
        resp.set_cookie('user_id', value=str(user_id), secure=True, httponly=True)
        return resp
    else:
        flash('Zły login lub hasło')
        return redirect(url_for('user_bp.login'))


@user_bp.route("/login", methods=['POST'])
def add_user():
    """Check if user with given email doesn't exist and if not, add new user to the database, set user cookies
     and return its library page."""
    email = request.form['login']
    password = request.form['password']
    if DatabaseOperations.check_if_email_exists(email):
        flash('Użytkownik z danym mailem już istnieje!')
        return redirect(url_for('user_bp.register'))
    else:
        user_id = DatabaseOperations.add_user(email, password)
        resp = make_response(render_template(LIBRARY, email=email, user_id=user_id))
        resp.set_cookie('email', value=email, secure=True, httponly=True)
        resp.set_cookie('user_id', value=str(user_id), secure=True, httponly=True)
        return resp


@user_bp.route("/readBooks", methods=['GET'])
def get_books():
    return WolneLekturyAPI.books_list


@user_bp.route("/addBook/<book_id>", methods=['GET'])
def add_book(book_id):

    user_id = request.cookies.get('user_id')
    email = request.cookies.get('email')

    if user_id is None:
        flash(NOT_LOGGED)
        return redirect(url_for(INDEX))
    else:
        if not DatabaseOperations.get_one_book(user_id=user_id,book_id=book_id):
            DatabaseOperations.add_book_to_library(user_id=user_id, book_id=book_id)
        return render_template(LIBRARY, email=email, user_id=user_id)


@user_bp.route("/fetchUserBooks")
def fetch_books():

    user_id = request.cookies.get('user_id')
    if user_id is None:
        flash(NOT_LOGGED)
        return redirect(url_for(INDEX))

    books = DatabaseOperations.get_book_from_library(user_id)
    books_id = [book[0].book_id for book in books]
 
    all_books = WolneLekturyAPI.books_list
    my_books = list(filter(lambda c: c['id'] in books_id, all_books))
    return my_books
    

@user_bp.route("/removeBook/<book_id>", methods=['GET'])
def remove_book(book_id):

    user_id = request.cookies.get('user_id')
    email = request.cookies.get('email')

    if user_id is None:
        flash(NOT_LOGGED)
        return redirect(url_for(INDEX))
    else:
        DatabaseOperations.remove_book_from_library(user_id=user_id, book_id=book_id)
        return render_template(LIBRARY, email=email, user_id=user_id)
