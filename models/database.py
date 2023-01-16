import os
import sys

from sqlalchemy import Column, Integer, String
from initialize_objects import db

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")


class User(db.Model):
    """
    Table where user accounts are stored

    Columns
    -------
    user_id : Integer
        Auto-generated primary key
    email : String(255)
        User email
    password : String(255)
        Hashed user password (Do not store plain passwords!)
    """
    user_id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(255))


class Book(db.Model):
    """
    Table where books added to user library are stored

    Columns
    -------
    uniq_id : Integer
        Auto-generated primary key
    user_id : Integer
        User that added book to its library
    book_id : Integer
        Book that is being added to user library
    """
    uniq_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    book_id = Column(Integer)
