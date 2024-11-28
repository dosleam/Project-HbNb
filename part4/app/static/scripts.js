// ROUTE API ================================================================================== //

const API_URL = 'http://127.0.0.1:5000/api/v1/auth/login';
const GET_ALL_PLACES = 'http://127.0.0.1:5000/api/v1/places';
const GET_PLACE = 'http://127.0.0.1:5000/api/v1/places';
const POST_REVIEW = 'http://127.0.0.1:5000/api/v1/reviews';
const GET_REVIEWS_FROM_PLACE = 'http://127.0.0.1:5000/api/v1/reviews/places';
const GET_USER_BY_ID = 'http://127.0.0.1:5000/api/v1/users';


// URL HTML =================================================================================== //

const LOGIN_PAGE_URL = 'http://127.0.0.1:5500/part4/app/templates/login.html';
const INDEX_PAGE_URL = 'http://127.0.0.1:5500/part4/app/templates/index.html';
const PLACE_PAGE_URL = 'http://127.0.0.1:5500/part4/app/templates/place.html';
const REVIEW_PAGE_URL = 'http://127.0.0.1:5500/part4/app/templates/add_review.html';

const LOGIN = 'login.html';
const INDEX = 'index.html';
const PLACE = 'place.html';
const ADD_REVIEW = 'add_review.html';

// AUTH ======================================================================================= //

// Fonction qui vérifie si l'utilisateur est loggé ou non
function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');
  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
}
}
// Fonction pour récupérer le cookie et ainsi vérifier si l'utilisateur est loggé
function getCookie(name) {
  const cookies = document.cookie.split(";");
  for (const cookie of cookies) {
    if (cookie.startsWith(name + "=")) {
      return cookie.substring(name.length + 1);
    }
  }
  return null;
}
// Fonction pour afficher ou non la section "Add Review" dans la page place.html si l'utilisateur est loggé
function displayAddReview() {
  const token = getCookie('token');
  const addReviewSection = document.getElementById('add-review');
  if (!token) {
    addReviewSection.style.display = 'none';
  } else {
    addReviewSection.style.display = 'block';
  }
}
// Fonction pour récupérer un utilisateur
async function getUser(id) {
  const requestUrl = `${GET_USER_BY_ID}/${id}`;
  const token = getCookie('token');
  try {
    const response = await fetch(requestUrl, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });
    if (!response.ok) {
      throw new Error(`Erreur HTTP ! statut : ${response.status}`);
    }
    const data = await response.json();
    const user = `${data.first_name} ${data.last_name}`;
    return user;

  } catch (error) {
    console.error('Erreur lors de la récupération de l\’utilisateur :', error);
    return null;
  }
}

async function getUserId() {
  const token = getCookie('token');

  // Decode the JWT token to get the user ID
  const tokenParts = token.split('.');
  if (tokenParts.length !== 3) {
    throw new Error('Invalid token');
  }

  const payload = JSON.parse(atob(tokenParts[1]));
  return payload.sub.id;

}

// LOGIN ====================================================================================== //

// Fonction pour gérer les cookies
function setAuthCookie(token) {
    const expiryDate = new Date();
    expiryDate.setDate(expiryDate.getDate() + 7);
    // crée un cooke avec le token et la date d'expiration disponible sur tout le site mais uniquement pour le site
    document.cookie = `token=${token}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Strict`;
}

function loginLoad() {
    // Récupère le formulaire de login par son ID CSS
    const loginForm = document.getElementById('login-form');

    // si l'id existe dans la page
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // empêche le rechargement par défaut de la page après avoir submit les infos du login

            try {
                // Récupère les données du formulaire
                const formData = new FormData(event.target);
                // Envoie la requête au serveur
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    // Convertit les données du formulaire en JSON
                    body: JSON.stringify({
                        email: formData.get('email'),
                        password: formData.get('password')
                    })
                });
                // Récupère la réponse du serveur en JSON
                const data = await response.json();

                // Vérifie si la connexion est réussie
                if (response.ok && data.access_token) {
                    // Sauvegarde le token dans un cookie en appelant la fonction setAuthCookie
                    setAuthCookie(data.access_token);
                    // Redirige vers la page principale
                    window.location.href = 'index.html';
                } else {
                    const errorElement = document.getElementById('error-message');
                    if (errorElement) {
                        errorElement.textContent = data.message || 'Connection failed.';
                        errorElement.style.display = 'block';
                    } else {
                        alert('Connection failed.');
                    }
                }
            } catch (error) {
                console.error('Login error:', error);
                alert('Error during connection.');
            }
        });
    }
}

// INDEX ====================================================================================== //

// inutile mais harmonise le nom des fonctions de base dans le DOMContentLoader
function indexLoad() {
  fetchPlaces();
}

// PLACES INDEX =============================================================================== //

// fonction pour récupérer la liste de places dans la DB
async function fetchPlaces() {
  try {
    // Effectue une requête API pour récupérer tous les lieux
    const response = await fetch(GET_ALL_PLACES);

    if (!response.ok) {
      throw new Error(`Erreur HTTP : ${response.status}`);
    }

    // Convertit le contenu de la réponse au format JSON et appelle une fonction pour l'afficher
    const places = await response.json();
    displayPlaces(places);
    return places;

  } catch (error) {
    console.error('Erreur de chargement des places :', error);
  }
}

function displayPlaces(places) {
  // récupère l'id "place-list" de la balise section de index.html
  const placesList = document.getElementById('places-list');
  // vide le contenu existant dans la section
  placesList.innerHTML = '';
  // boucle dans le dictionnaire "places", crée un élément div pour chaque lieu ajoute des class CSS pour le style
  // crée un attribut personnalisé pour le prix du lieu (pour le trier plus tard) et l'id de la place puis rempli le contenue HTML avec les infos du lieu
  places.forEach(place => {
    const placeElement = document.createElement('div');
    placeElement.classList.add('card', 'place-card');
    placeElement.dataset.price = place.price;
    placeElement.dataset.placeId = place.id;
    placeElement.innerHTML = `
      <h3 class="place-name">${place.title}</h3>
      <p class="place-price">Price per night: $${place.price}</p>
      <a href="place.html?place_id=${place.id}" class="button login-button">View Details</a>`;
    // Ajoute l'élément
    placesList.appendChild(placeElement);
  });
  priceFilter();
}

// PRICES FILTERING INDEX ===================================================================== //

function priceFilter() {
  const priceSelect = document.getElementById('price-filter'); // récup filtre
  const placeCards = document.querySelectorAll('.place-card'); // récup les cartes de lieux

  // regarde si le filtre change si oui convertie la valeur en int
  priceSelect.addEventListener('change', (event) => {
    const selectedPrice = parseInt(event.target.value); // Convertir en nombre

    placeCards.forEach(card => { // Parcourt toutes les cartes
      const placePrice = parseInt(card.dataset.price); // Récup prix stocké dans la carte du lieu

      // si le prix de la place est inférieur ou égal au prix selectionné (0 si 'All' est select)
      if (selectedPrice === 0 || placePrice <= selectedPrice) {
        card.classList.remove('hidden'); // supprime la class hidden
      } else { // sinon
        card.classList.add('hidden'); // ajoute la class hidden
      }
    });
  });
}

// PLACE ====================================================================================== //

async function placeLoad() {
  try {
    displayAddReview();
    const placeData = await getPlaceIdFromURL();
    displayPlaceInfos(placeData);
  } catch (error) {
    console.error('Erreur lors du chargement:', error);
  }
}

async function getPlaceIdFromURL() {
  try {
    const url = new URL(window.location.href);
    const placeId = url.searchParams.get('place_id');
    const token = getCookie('token');
    const requestUrl = `${GET_PLACE}/${placeId}`;

    // Appel API avec fetch
    const response = await fetch(requestUrl, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    // Vérification de la réponse
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status} - ${await response.text()}`);
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error('Erreur dans getPlaceIdFromURL:', error);
    throw error;
  }
}

async function displayPlaceInfos(data) {
  const placeBucket = document.getElementById('place-details'); // Cible la section existante
  placeBucket.innerHTML = ''; // Vide le contenu actuel pour le remplacer

  // Ajout du titre
  const placeTitle = document.createElement('h1');
  placeTitle.textContent = data.title || 'Unknown Title'; // Utilise une clé "title" ou une valeur par défaut
  placeBucket.appendChild(placeTitle);

  // Création de la carte de détails
  const placeElement = document.createElement('div');
  placeElement.classList.add('details-card');

  // Ajout des informations dynamiques
  placeElement.innerHTML = `
    <p><strong>Host:</strong> ${await getUser(data.owner_id) || 'Unknown Host'}</p>
    <p><strong>Price per night:</strong> $${data.price || 'N/A'}</p>
    <p><strong>Description:</strong> ${data.description || 'No description available.'}</p>
    <p><strong>Amenities:</strong> ${data.amenities ? data.amenities.map(amenity => amenity.name).join(', ') : 'No amenities listed.'}</p>
  `;

  placeBucket.appendChild(placeElement); // Ajout de la carte à la section
  displayPlaceReviews(data); // appelle la fonction pour afficher les reviews de la place
}

async function displayPlaceReviews(placeData) {
  const reviewsList = document.getElementById('reviews');
  reviewsList.innerHTML = '';
  try {
    const placeId = placeData.id;
    const requestUrl = `${GET_REVIEWS_FROM_PLACE}/${placeId}`;

    // Effectuer la requête pour obtenir les données de reviews
    const response = await fetch(requestUrl);
    if (!response.ok) {
      const titleElement = document.createElement('h2');
      titleElement.textContent = 'Reviews';
      reviewsList.appendChild(titleElement);
      const reviewCard = document.createElement('div');
      reviewCard.classList.add('review-card');
      reviewCard.innerHTML += `<p>No reviews available for this place.</p>`;
      reviewsList.appendChild(reviewCard);
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reviewsData = await response.json();

    loadReviews(reviewsData);

  } catch (error) {
    console.error("Error fetching reviews:", error);
  }
}

async function loadReviews(datas) {
  const reviewsList = document.getElementById('reviews');

  // Vide tout le contenu existant (y compris le titre)
  reviewsList.innerHTML = '';

  // Ajout du titre de la section
  const titleElement = document.createElement('h2');
  titleElement.textContent = 'Reviews';
  reviewsList.appendChild(titleElement);

  // Ajout dynamique des cartes de review
  for (const data of datas) {
    const reviewCard = document.createElement('div');
    reviewCard.classList.add('review-card');

    // Remplit le contenu de la carte
    reviewCard.innerHTML = `
      <p><strong>${await getUser(data.owner_id)}:</strong></p>
      <p>${data.text}</p>
      <p>Rating: ${'★'.repeat(data.rating)}${'☆'.repeat(5 - data.rating)}</p>
    `;

    // Ajoute la carte au conteneur
    reviewsList.appendChild(reviewCard);
  }
}

async function addReview() {
  const reviewForm = document.getElementById('review-form');
  // Crée un div pour afficher les erreurs ================== //
  const errorMessageElement = document.createElement('div');
  // Style //
  errorMessageElement.style.color = 'red';
  errorMessageElement.style.marginTop = '10px';
  // Ajouté dans l'élément review-form //
  reviewForm.appendChild(errorMessageElement);
  // ======================================================== //
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      errorMessageElement.textContent = '';
      try {
        const url = new URL(window.location.href);
        const placeId = url.searchParams.get('place_id');
        const ownerId = await getUserId();
        const token = getCookie('token');

        const formData = new FormData(event.target);

        const response = await fetch(POST_REVIEW, {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Origin': window.location.origin
            },
            body: JSON.stringify({
              text: formData.get('review-text'),
              rating: Number(formData.get('rating')),
              owner_id: ownerId,
              place_id: placeId
          })
        });

        // Gestion des réponses non-OK
        if (!response.ok) {
          const errorText = await response.text();
          console.error('Server response:', errorText);

          // si le status de la reponse est 409 (doublon)
          if (response.status === 409) {
            errorMessageElement.textContent = 'You have already posted a review for this establishment.';
            return;
          }

          if (response.status === 403) {
            errorMessageElement.textContent = 'You cannot leave a review for your own establishment.';
            return;
          }

          // Pour les autres types d'erreurs, on lance une exception
          throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }

        const result = await response.json();
        console.log('Review submitted successfully', result);

        reviewForm.reset();

      // erreur du try
      } catch (error) {
        console.error('Error submitting review:', error);
        errorMessageElement.textContent = 'An error occurred while submitting your review.';
      }
    });
  }
}

// REVIEW ===================================================================================== //

function reviewLoad() {
  console.log("review")
}

// LOADER ===================================================================================== //

document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();

  // Récupère le nom du fichier depuis l'URL
  const currentPage = window.location.pathname.split('/').pop();
  if (currentPage === LOGIN) {
    loginLoad();
  }

  if (currentPage === INDEX) {
    indexLoad();
  }

  if (currentPage === PLACE) {
    placeLoad();
    addReview();
  }

  if (currentPage === ADD_REVIEW) {
    reviewLoad();
  }
});
