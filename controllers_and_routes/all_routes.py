import sys
import os
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

@user_bp.route("/api")
def simple_query():
    # https://flask-restless.readthedocs.io/en/stable/searchformat.html
    url  = "https://wolnelektury.pl/api/authors/adam-mickiewicz/kinds/liryka/books/"
    headers = {'Content-Type': 'application/json'}

    filters = [dict(name='name', op='like', val='%y%')]
    params = dict(q=json.dumps(dict(filters=filters)))

    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
    print(response.json())

    return "first record: </br>" + str(response.json()[0])

@user_bp.route("/user")
def user():
    return render_template("user.html")