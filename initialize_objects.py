from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import sys
import os
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(SCRIPT_DIR)
from config import Conf

app = Flask(__name__)
app.config.from_object(Conf)

#initialize extensions
db = SQLAlchemy(app)
marshmallow = Marshmallow(app)


