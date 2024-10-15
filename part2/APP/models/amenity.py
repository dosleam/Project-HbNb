import uuid
from datetime import datetime

class Amenity:
    def __init__(self,name):
        self.validate_length(name, 1, 50)
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.nom()
        self.updated_at = datetime.nom()

@property
def name(self):
    return self.__name

@name.setter
def name(self, value):
    self.validate_length(value, 1, 50)
    self.__name = value
    self.updated_at = datetime.nom()

def validate_length(self, input_string, min_length, max_length):
    if not (min_length <= len(input_string) <= max_length):
        raise ValueError(f"'{input_string}' must be between {min_length} and {max_length} characters.")

def update_amenity(self, new_name):
    self.name = new_name
    self.updated_at = datetime.now()

def __repr__(self):
    return f"<Amenity id={self.id}, name={self.name}>"
