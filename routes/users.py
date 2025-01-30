from flask import Blueprint, jsonify, request
from models.user import User
from database import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

users_bp = Blueprint('users', __name__, url_prefix='/user')

@users_bp.route('/information', methods=['GET'])
@jwt_required()
def list_users():

    try:
        
        user_id = get_jwt_identity()

        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "The user doesn't exist"}), 404

        return jsonify({
            "message": "success",
            "user" : {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "created_at" : user.created_at 
            }
        }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)})
    
    
@users_bp.route('/change-password', methods=['PUT'])
@jwt_required()
def change_password():

    try:
        user_id = get_jwt_identity()
        data = request.get_json()

        if not data.get('password') or not data.get('new_password'):
            return jsonify({"message": "Missing required fields (password, new_password)"}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "The user doesn't exist"})

        if not check_password_hash(user.password, data['password']):
            return jsonify({"message": "The password doesn't match"}), 401

        hashed_password = generate_password_hash(data['new_password'])
        
        user.password = hashed_password
        db.session.commit()

        return jsonify({"message": "success"}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

        
@users_bp.route('/information', methods=['PUT'])
@jwt_required()
def update_user():
    
    try:
        user_id = get_jwt_identity()
        data = request.get_json()

        if not data.get('name') or not data.get('email'):
            return jsonify({"message": "Missing required fields (name, email)"})

        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "The user doesn't exist"}), 401

        user.name = data['name']
        user.email = data['email']
        user.updated_at = datetime.now()

        db.session.commit()

        return jsonify({
            "message": "success",
            "user" : {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email
            }
        }), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500
    