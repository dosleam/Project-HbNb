import uuid
from datetime import datetime


class Place:
    def __init__(self, title, price, latitude, longitude, owner, description=None):

        self.input_length_validation(title, 1, 100)
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.description = description
        self.reviews = []
        self.amenities = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("The price must be positive")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not -180 <= value <= 180:
            raise ValueError("Latitude must be between -180 and 180")
        self.__longitude = value

    def update_place(self, new_title, price, latitude, longitude, owner, new_description=None):

        self.is_valid_length(new_title, 1, 100)
        self.title = new_title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.description = new_description
        self.updated_at = datetime.now()

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def is_valid_length(self, input, min, max):
        if not (min <= len(input) <= max):
            raise ValueError(f"{input} be between {min} and {max} characters.")
