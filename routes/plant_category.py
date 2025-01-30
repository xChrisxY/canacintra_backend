from flask import Blueprint, jsonify, request
from models.plant_category import PlantCategory
from models.plant_group import PlantGroup
from models.optimal import Optimal
from database import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

plant_category_bp = Blueprint('plant_category', __name__, url_prefix='/plant_category')

@plant_category_bp.route('/categories/<string:category_id>', methods=['GET'])
@jwt_required()
def get_all_plants_category(category_id):
    
    try:

        plant_category = (
            db.session.query(PlantCategory)
            .join(PlantGroup, PlantCategory.plant_group_id == PlantGroup.id)
            .join(Optimal, db.or_(
                PlantGroup.optimal_temp_id == Optimal.id,
                PlantGroup.optimal_humidity_id == Optimal.id,
                PlantGroup.optimal_ph_id == Optimal.id,
                PlantGroup.optimal_ec_id == Optimal.id,
            ))
            .filter(PlantCategory.id == category_id)
            .first()
        )
        
        if not plant_category:
            return jsonify({"message": "Plant category not found"}), 404

        print(plant_category)

        response = {
            "id": plant_category.id,
            "name": plant_category.name,
            "harvestDays": plant_category.harvest_days,
            "image": plant_category.image,
            "group": {
                "id": plant_category.plant_group.id,
                "name": plant_category.plant_group.name,
                "optimal": {
                    "temperature": {
                        "value": plant_category.plant_group.optimal_temp.value,
                        "min": plant_category.plant_group.optimal_temp.min,
                        "max": plant_category.plant_group.optimal_temp.max
                    },
                    "humidity": {
                        "value": plant_category.plant_group.optimal_humidity.value,
                        "min": plant_category.plant_group.optimal_humidity.min,
                        "max": plant_category.plant_group.optimal_humidity.max
                    },
                    "ph": {
                        "value": plant_category.plant_group.optimal_ph.value,
                        "min": plant_category.plant_group.optimal_ph.min,
                        "max": plant_category.plant_group.optimal_ph.max
                    },
                    "ec": {
                        "value": plant_category.plant_group.optimal_ec.value,
                        "min": plant_category.plant_group.optimal_ec.min,
                        "max": plant_category.plant_group.optimal_ec.max
                    }
                }
            }
        }

        return jsonify({"message": "success", "plant category": response})
        
    except Exception as e:
        return jsonify({"message": str(e)})
    