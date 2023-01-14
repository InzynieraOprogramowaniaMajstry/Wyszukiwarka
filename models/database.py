import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")


from sqlalchemy import Column, Integer, String, ForeignKey
from initialize_objects import db

class User(db.Model):
    user_id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(255))


class Book(db.Model):
    uniq_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    book_id = Column(Integer)