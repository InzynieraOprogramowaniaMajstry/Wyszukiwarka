import sys
import os
from models.wolne_lektury_api import WolneLekturyAPI
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")

from flask import Blueprint
user_bp = Blueprint('user_bp', __name__)

import requests
from flask import json, render_template

@user_bp.route("/")
def index():
    return render_template("base.html")

@user_bp.route("/login")
def login():
    return render_template("login.html")


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