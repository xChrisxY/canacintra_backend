from flask import Blueprint, jsonify, request
from models.plant import Plant
from models.hydroponic_systems import HydroponicSystem
from database import db 
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

plant_bp = Blueprint('plant', __name__, url_prefix='/plant')

@plant_bp.route('/create', methods=['POST'])
@jwt_required()
def create_plant():

    try:
    
        data = request.get_json()
        
        required_fields = ['categoryId', 'hydroponicSystemId', 'estimatedHarvest']
        for field in required_fields:
            if field not in data:
                return jsonify({"message": "f{field} es un campo requerido"}), 400

                
        try:
            estimated_harvest = datetime.strptime(data['estimatedHarvest'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"message": "Invalid Format Date. Use YYYY-MM-DD"})

                
        new_plant = Plant(
            category_id = data['categoryId'],
            hydroponic_system_id = data['hydroponicSystemId'],
            status = "creciendo",
            estimated_harvest = estimated_harvest
        )
        
        
        db.session.add(new_plant)
        db.session.commit()

        return jsonify({
            "message": "Plant created successfully",
            "plant" : {
                "id" : new_plant.id,
                "categoryId" : new_plant.category_id,
                "hydroponicSystemId" : new_plant.hydroponic_system_id,
                "status" : new_plant.status,
                "estimated_harvest": new_plant.estimated_harvest.strftime("%Y-%m-%d"),
                "created_at": new_plant.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": new_plant.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        db.session.close()

@plant_bp.route('/harvested', methods=['GET'])
@jwt_required()
def get_cooked_plants():
    
    try:

        user_id = get_jwt_identity()

        harvested_plants = (
            db.session.query(Plant)
            .join(HydroponicSystem, Plant.hydroponic_system_id == HydroponicSystem.id)
            .filter(HydroponicSystem.user_id == user_id, Plant.status == "creciendo")
            .all()
        )

        print(harvested_plants)

        result = [
            {
                "id": plant.id,
                "categoryId": plant.category_id,
                "hydroponicSystemId": plant.hydroponic_system_id,
                "status": plant.status,
                "estimatedHarvest": plant.estimated_harvest,
                "createdAt": plant.created_at,
                "updatedAt": plant.updated_at
            }
            for plant in harvested_plants
        ]

        return jsonify({"message": "success", "harvestedPlants": result}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    