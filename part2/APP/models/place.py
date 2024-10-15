import uuid
from datetime import datetime

class Place:
    def __init__(self, title, price, latitude, longitude, owner, description=None):
        self.validate_length(title, 1, 100)
        self.validate_user_instance(owner)
        self.validate_float(price)
        self.validate_float(latitude)
        self.validate_float(longitude)

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
            raise ValueError("The price must be positive.")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        self.__longitude = value

    def update_place(self, new_title, price, latitude, longitude, owner, new_description=None):
        self.validate_length(new_title, 1, 100)
        self.validate_user_instance(owner)

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

    def validate_length(self, input_value, min_length, max_length):
        if not (min_length <= len(input_value) <= max_length):
            raise ValueError(f"The input must be between {min_length} and {max_length} characters.")

    def validate_user_instance(self, owner):
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance.")

    def validate_float(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Expected a float or int value, but got {type(value).__name__}.")
