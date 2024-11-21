document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault(); // Empêcher la soumission par défaut du formulaire

          // Récupération des valeurs des champs email et password
          const email = document.getElementById('email').value;
          const password = document.getElementById('password').value;

          try {
              // Appel de la fonction pour faire la requête de connexion
              const success = await loginUser(email, password);

              if (success) {
                  // Redirection vers la page principale après une connexion réussie
                  window.location.href = 'index.html';
              } else {
                  // Affichage d'un message d'erreur si la connexion échoue
                  displayErrorMessage('Échec de la connexion. Veuillez vérifier vos identifiants.');
              }
          } catch (error) {
              // Gestion des erreurs inattendues
              displayErrorMessage('Une erreur est survenue. Veuillez réessayer plus tard.');
              console.error('Erreur lors de la connexion:', error);
          }
      });
  }
});

// Fonction pour faire une requête de connexion
async function loginUser(email, password) {
  try {
      const response = await fetch('https://your-api-url/login', { // Remplacez 'your-api-url' par l'URL de votre API
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
      });

      if (response.ok) {
          const data = await response.json();
          
          // Stocker le token JWT dans un cookie
          document.cookie = `token=${data.access_token}; path=/; secure; SameSite=Strict`;

          return true; // Connexion réussie
      } else {
          return false; // Connexion échouée
      }
  } catch (error) {
      console.error('Erreur lors de la requête de connexion:', error);
      return false;
  }
}

// Fonction pour afficher un message d'erreur à l'utilisateur
function displayErrorMessage(message) {
  let errorElement = document.getElementById('error-message');

  if (!errorElement) {
      // Créer un élément pour le message d'erreur s'il n'existe pas encore
      errorElement = document.createElement('div');
      errorElement.id = 'error-message';
      errorElement.style.color = 'red';
      errorElement.style.marginTop = '10px';
      loginForm.appendChild(errorElement);
  }

  // Afficher le message d'erreur
  errorElement.textContent = message;
}
