from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
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

        # Check if the email is already registered
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            # Create the new user with hashed password
            new_user = facade.create_user(user_data)
        except ValueError as e:
            return {"error": "An unexpected error occurred: " + str(e)}, 500

        # Return user details without the password
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email,
        }, 201

    def get(self):
        """Retrieve a list of all users"""
        return [
            { "id": user.id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email }
            for user in facade.get_all_users()
        ]

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        # Exclude password from the response
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    @api.response(400, 'You cannot modify email or password')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        payload = api.payload
        if "email" in payload or "password" in payload:
            return {"error": "You cannot modify email or password"}, 400

        try:
            user = facade.update_user(user_id, api.payload)

            if not user:
                return {"error": "User not found"}, 404
            return { "id": user.id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email }
        except Exception as e:
            return {"error": "Invalid input data"}, 400
