from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.sensor import Sensor
from models.components import Components
from models.hydroponic_systems import HydroponicSystem
from database import db

hydroponic_system_bp = Blueprint('hydroponic_system', __name__, url_prefix='/hydroponic_system')

@hydroponic_system_bp.route('/user/<string:user_id>', methods=['GET'])
@jwt_required()
def hydroponic_system_by_user_id(user_id):

    try:
    
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "The user doesn't exist"}), 404

        hydroponic_system_by_user_id = HydroponicSystem.query.filter_by(user_id=user_id)

        results = []
        for hydro in hydroponic_system_by_user_id:
            results.append({
                "hydroponicSystemId" : hydro.id,
                "name": hydro.name,
                "createdAt" : hydro.created_at,
                "updatedAt" : hydro.updated_at, 
                "userId" : hydro.user_id 
            })

        return jsonify({"message": "success", "hydroponicSystems": results}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@hydroponic_system_bp.route('/user/<string:user_id>', methods=['POST'])
@jwt_required()
def create_hydroponic_system(user_id):

    try: 
        data = request.get_json()
        
        if not data.get('name'):
            return jsonify({"message": "Missing requied fields"}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "The user doesn't exist"}), 404

        hydroponic_system = HydroponicSystem(name=data['name'], user_id=str(user_id))

        db.session.add(hydroponic_system)
        db.session.commit()

        ph = Components(1, 0, hydroponic_system.id) 
        temperatura = Components(2, 0,hydroponic_system.id) 
        conductividad = Components(3, 0,hydroponic_system.id) 
        nivel_de_agua = Components(4, 0,hydroponic_system.id) 
        humedad = Components(5, 0,hydroponic_system.id) 
        dispensador = Components(6, 0,hydroponic_system.id) 
        bomba = Components(7, 0, hydroponic_system.id)

        db.session.add(ph)
        db.session.add(temperatura)
        db.session.add(conductividad)
        db.session.add(nivel_de_agua)
        db.session.add(humedad)
        db.session.add(dispensador)
        db.session.add(bomba)

        db.session.commit()

        return jsonify({
            "message": "Sistema hidropónico creado exitosamente",
            "hydroponic_system": {
                "id" : str(hydroponic_system.id),
                "name" : str(hydroponic_system.name),
                "user_id" : str(hydroponic_system.user_id),
                "created_at" : str(hydroponic_system.created_at),
                "updated_at" : str(hydroponic_system.updated_at)
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        db.session.close()

@hydroponic_system_bp.route('/<string:id>', methods=['GET'])   
@jwt_required()
def hydroponic_system_by_id(id):

    try:

        hydroponic_system = HydroponicSystem.query.filter(HydroponicSystem.id==id).first()

        if hydroponic_system is None:
            return jsonify({"message": "Hydroponic System not found"}), 404

        return jsonify({
            "message": "Success",
            "hydroponic_system" : {
                "id" : str(hydroponic_system.id),
                "name" : str(hydroponic_system.name),
                "user_id" : str(hydroponic_system.user_id),
                "created_at" : str(hydroponic_system.created_at),
                "updated_at" : str(hydroponic_system.updated_at)
            }
        })

    except Exception as e:
        return jsonify({"error" : str(e)}), 500


    
    
    

