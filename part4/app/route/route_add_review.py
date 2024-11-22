from flask import Blueprint, render_template, request, url_for, redirect

add_review_bp = Blueprint('add_review_bp', __name__)

# Route pour ajouter un avis (add_review.html)
@add_review_bp.route('/add_review.html', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        # Récupérer les données du formulaire d'avis
        review_text = request.form['review']
        rating = request.form['rating']
        
        # Logique pour enregistrer l'avis dans la base de données
        
        return redirect(url_for('index'))  # Redirige vers la page d'accueil
    
    return render_template('add_review.html')
