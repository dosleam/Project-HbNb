from flask import Blueprint, render_template, request

place_bp = Blueprint('place_bp', __name__)

# Route pour la page de détails d'un endroit
@place_bp.route('/place.html')
def place():
    place_id = request.args.get('place_id')
    # Utilisez place_id si nécessaire
    return render_template('place.html', place_id=place_id)

