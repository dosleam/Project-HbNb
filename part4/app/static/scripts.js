document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message'); // Élément pour afficher le message d'erreur

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();  // Empêche le rechargement de la page lors de la soumission du formulaire

            // Récupérer les valeurs du formulaire
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Réinitialiser le message d'erreur à chaque tentative de connexion
            errorMessage.textContent = '';

            // Appeler la fonction pour se connecter
            await loginUser(email, password);
        });
    }
});

async function loginUser(email, password) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/auth/login', {  // Remplace 'ton-api-url' par l'URL de l'API
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        // Vérifier la réponse de l'API
        if (response.ok) {
            const data = await response.json();
            
            // Stocker le token JWT dans un cookie
            document.cookie = `token=${data.access_token}; path=/`;

            // Rediriger l'utilisateur vers la page d'accueil après une connexion réussie
            window.location.href = 'index.html';
        } else {
            // Afficher un message d'erreur si la connexion échoue
            const errorData = await response.json();
            showError(`Échec de la connexion : ${errorData.message || 'Informations incorrectes.'}`);
        }
    } catch (error) {
        // En cas d'erreur réseau ou autre
        console.error('Erreur lors de la tentative de connexion:', error);
        showError('Une erreur est survenue. Veuillez réessayer plus tard.');
    }
}

// Fonction pour afficher le message d'erreur sur la page
function showError(message) {
    const errorMessage = document.getElementById('error-message');
    if (errorMessage) {
        errorMessage.textContent = message;
    } else {
        alert(message);  // En cas de problème avec l'affichage, utilisez alert comme fallback
    }
}
