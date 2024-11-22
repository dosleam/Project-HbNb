from flask import Blueprint, render_template

place_bp = Blueprint('place_bp', __name__)

# Route pour la page de détails d'un endroit
@place_bp.route('/place/<int:place_id>')
def place(place_id):
    places = {
        1: {
            "name": "Beautiful Beach House",
            "host": "John Doe",
            "price": "$150",
            "description": "A beautiful beach house with amazing views...",
            "amenities": "WiFi, Pool, Air Conditioning"
        },
        2: {
            "name": "Cozy Cabin",
            "host": "Jane Doe",
            "price": "$100",
            "description": "A cozy cabin in the woods, perfect for a weekend getaway.",
            "amenities": "Fireplace, Kitchen, Outdoor Space"
        },
        3: {
            "name": "Modern Apartment",
            "host": "Michael Smith",
            "price": "$200",
            "description": "A stylish apartment in the city with great views.",
            "amenities": "WiFi, Gym, Parking"
        }
    }
    place = places.get(place_id)
    return render_template('place.html', place=place)

