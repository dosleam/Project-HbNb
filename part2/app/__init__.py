from flask import Flask
from flask_restx import Api
from app.api.v1.reviews import api as reviews_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    api.add_namespace(reviews_ns, path="/api/v1/reviews")

    # Placeholder for API namespaces (endpoints will be added later)
    # Additional namespaces for places, reviews, and amenities will be added later

    return app