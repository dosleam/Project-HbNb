from .base import BaseModel
from app import bcrypt
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password  # Utilise le setter pour hacher le mot de passe
        self.is_admin = is_admin
        self.places = []

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

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            raise ValueError("You must enter an email")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if value is None or len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        # Hacher le mot de passe avant de le stocker
        self._password = bcrypt.generate_password_hash(value).decode('utf-8')

    def verify_password(self, password):
        """Vérifie si le mot de passe fourni correspond au mot de passe haché."""
        return bcrypt.check_password_hash(self._password, password)

    def add_place(self, place):
        """Add a place to the user"""
        self.places.append(place)
