from flask import Blueprint, jsonify, request
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    
    data = request.get_json()

    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Missing required fields"}), 400

    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"message": "Email is already registered"}), 400

    hashed_password = generate_password_hash(data['password'])

    new_user = User(name=data['name'], email=data['email'], password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=str(new_user.id))

    return jsonify({"message": "User registered succesfully", "access_token":access_token}), 201

    
@auth_bp.route('/login', methods=['POST'])
def login():

    try:
    
        data = request.get_json()

        if not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Missing required fields'}), 400

        user = User.query.filter_by(email=data['email']).first()

        if not user:
            return jsonify({"message": "Invalid email or password"}), 401

        if not check_password_hash(user.password, data['password']):
            return jsonify({'message': 'Invalid email or password'}), 401

        access_token = create_access_token(identity=str(user.id))

        username = User.query.filter_by(id=str(user.id)).first()

        return jsonify({"name": str(username),"access_token": access_token}), 200

    except Exception as e:
        return jsonify({"error": str(e)})

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    
    user_id = get_jwt_identity()
    return jsonify({"message": f"Hello, user {user_id}!"}), 200