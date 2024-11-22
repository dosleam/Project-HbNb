from flask import Blueprint, render_template, request, redirect, url_for, jsonify

login_bp = Blueprint('login_bp', __name__)

# Simuler une base de données utilisateur
USER_DATABASE = {
    'jeremy.sousa@outlook.fr': {
        'password': 'Dosletal',  # Remplace par une vraie logique de génération de token
    }
}

# Route pour la page de connexion (login.html)
@login_bp.route('/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Vérification des identifiants
    if email in USER_DATABASE and USER_DATABASE[email]['password'] == password:
        token = USER_DATABASE[email]['token']
        return jsonify({'access_token': token}), 200  # Renvoie un token si l'authentification réussit
    else:
        return jsonify({'message': 'Email ou mot de passe incorrect'}), 401

# Route pour servir la page de connexion
@login_bp.route('/login.html', methods=['GET'])
def login_page():
    return render_template('login.html')
