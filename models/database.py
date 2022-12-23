import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append("..")


from sqlalchemy import Column, Integer, String, Float
from initialize_objects import db, marshmallow

class User(db.Model):
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Books(db.Model):
    __tablename__ = "planets"
    book_id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    author = Column(String)

    

class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class BookSchema(marshmallow.Schema):
    class Meta:
        fields = ("book_id", "title", "author" )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = BookSchema()
planets_schema = BookSchema(many=True)