from .base import BaseModel
from flask_bcrypt import Bcrypt
import re
from app import db, bcrypt
import uuid
from .base_model import BaseModel

bcrypt = Bcrypt()

class User(BaseModel):

    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self._password = None
        self.hash_password(password)

    # Property and setter for first_name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value is None:
            raise ValueError("You must enter a first name")
        if len(value) > 50:
            raise ValueError("First name must not exceed 50 characters")
        self._first_name = value

    # Property and setter for last_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is None:
            raise ValueError("You must enter a last name")
        if len(value) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        self._last_name = value

    # Property and setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            raise ValueError("You must enter an email")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid input data")
        self._email = value

    # Property and setter for password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_password):
        self.hash_password(plain_password)

    def hash_password(self, plain_password):
        hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')
        self._password = hashed_password

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def add_place(self, place):
        self.places.append(place)
