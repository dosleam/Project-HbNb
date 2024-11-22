from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # Import de CORS
from datetime import timedelta
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.admin import api as admin_ns
from app.extensions import db, bcrypt
from app.route.route_index import home_bp
from app.route.route_login import login_bp
from app.route.route_place import place_bp
from app.route.route_add_review import add_review_bp

jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    """
    Factory function to create and configure the Flask app instance.

    :param config_class: The configuration class to use. Defaults to DevelopmentConfig.
    :return: Configured Flask app instance.
    """
    # Initialize the Flask application
    app = Flask(__name__)

    # Enable CORS for the app
    CORS(app)  # Ajout de la gestion de CORS pour toutes les routes

    # Load the configuration from the provided class
    app.config.from_object(config_class)

    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # Initialize the API with Flask-RESTX
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    api.add_namespace(reviews_ns, path="/api/v1/reviews")
    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenities_ns, path="/api/v1/amenities")
    api.add_namespace(auth_ns, path="/api/v1/auth")
    api.add_namespace(admin_ns, path="/api/v1/admin")
    
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(place_bp)
    app.register_blueprint(add_review_bp)

    return app
