from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Définir le modèle utilisateur pour la validation des entrées et la documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user', min_length=8)
})

user_response_model = api.model('UserResponse', {
    'id': fields.String(description='ID of the user'),
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Vérifier l'unicité de l'email
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            # Hacher le mot de passe avant de créer l'utilisateur
            password = user_data.pop('password')
            new_user = facade.create_user(user_data, password)
        except ValueError as e:
            return {"error": str(e)}, 400

        # Ne pas retourner le mot de passe dans la réponse
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201

    @api.marshal_list_with(user_response_model)
    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve all users"""
        users = facade.get_all_users()
        user_list = [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            } for user in users
        ]
        return user_list, 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        # Ne pas retourner le mot de passe dans la réponse
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user details by ID"""
        obj = facade.get_user(user_id)
        if not obj:
            return {"error": "User not found"}, 404

        try:
            user_data = api.payload
            # Si le mot de passe est présent, le hacher avant la mise à jour
            password = user_data.get('password')
            if password:
                facade.update_user(user_id, user_data, password)
            else:
                facade.update_user(user_id, user_data)
        except Exception as e:
            return {"error": "Invalid input data"}, 400

        return {"message": "User updated successfully"}, 200
