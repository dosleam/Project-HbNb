from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__)

# Route pour la page d'accueil (index.html)
@home_bp.route('/index.html')
def index():
    return render_template('index.html')
