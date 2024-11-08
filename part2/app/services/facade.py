from app.models import User  # Assurez-vous que User est correctement importé
from flask_bcrypt import Bcrypt
from app import bcrypt  # Assurez-vous que Bcrypt est bien initialisé

def get_all_users():
    """Retourne tous les utilisateurs"""
    return db_session.query(User).all()

def get_user(user_id):
    """Retourne un utilisateur par ID"""
    return db_session.query(User).filter_by(id=user_id).first()

def get_user_by_email(email):
    """Retourne un utilisateur par email"""
    return db_session.query(User).filter_by(email=email).first()

def create_user(user_data, password):
    """Crée un nouvel utilisateur en hachant le mot de passe"""
    # Crée un utilisateur avec les données fournies
    new_user = User(**user_data)
    # Hachage du mot de passe avant de le stocker
    new_user.hash_password(password)
    # Sauvegarde dans la base de données
    db_session.add(new_user)
    db_session.commit()
    return new_user

def update_user(user_id, user_data, password=None):
    """Met à jour un utilisateur existant, en hachant le mot de passe si nécessaire"""
    user = db_session.query(User).filter_by(id=user_id).first()
    if not user:
        return None

    # Met à jour les données de l'utilisateur
    for key, value in user_data.items():
        setattr(user, key, value)

    # Si un mot de passe est fourni, le hacher et le mettre à jour
    if password:
        user.hash_password(password)

    # Sauvegarde des modifications dans la base de données
    db_session.commit()
    return user
