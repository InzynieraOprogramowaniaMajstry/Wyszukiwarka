import sys
import os
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(SCRIPT_DIR)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.wolne_lektury_api import WolneLekturyAPI
from config import Conf

app = Flask(__name__)
app.config.from_object(Conf)
app.secret_key = b'wyszukiwarka_io_secret'

db = SQLAlchemy(app)
WolneLekturyAPI.fetch_api()
