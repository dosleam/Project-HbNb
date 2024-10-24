from .base import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def rating(self):
        return self._rating

    @text.setter
    def texting(self, value):
        if value is None:
            raise ValueError("You must enter a text")
        self.text = value

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value
