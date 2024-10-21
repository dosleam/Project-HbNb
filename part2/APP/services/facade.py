from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        pass

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        pass

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        pass

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        pass

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

def get_review(self, review_id):
    return self.review_repo.get(review_id)

def get_all_reviews(self):
    return self.review_repo.get_all()

def get_reviews_by_place(self, place_id):
    return self.review_repo.get_by_attribute('place', place_id)

def update_review(self, review_id, review_data):
    return self.review_repo.update(review_id, review_data)

def delete_review(self, review_id):
    return self.review_repo.delete(review_id)