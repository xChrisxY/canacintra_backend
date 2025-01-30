from flask import Blueprint, jsonify, request
from models.sensor import Sensor
from models.sensor_reading import SensorReading
from models.read import Read
from models.hydroponic_systems import HydroponicSystem
from models.components import Components
from database import db 
from datetime import datetime

sensor_reading_bp = Blueprint('sensor_reading', __name__, url_prefix='/sensor')

@sensor_reading_bp.route('/', methods=['POST'])
def create_sensor_reading():
    try:
        data = request.get_json()

        if not data.get('type') or not data.get('value'):
            return jsonify({"message": "Missing required fields (type, value)"}), 401

        sensor = Read(data['value'])
        db.session.add(sensor)
        db.session.commit()

        sensor_filter_by_type = Sensor.query.filter_by(type=data['type']).first()
        sensor_reading = SensorReading(sensor_filter_by_type.id, sensor.id)
        db.session.add(sensor_reading)
        db.session.commit()

        return jsonify({"message": "success"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        db.session.close()

        
@sensor_reading_bp.route('/hydroponic_system/<string:hydro_id>', methods=['GET'])
def get_sensor_by_hydroponic_system(hydro_id):
    
    try:

        hydro_system = HydroponicSystem.query.filter_by(id=hydro_id).first()

        if not hydro_system:
            return jsonify({"message": "Hydroponic System not found"}), 404

        components = Components.query.filter_by(hydroponic_system_id=hydro_id).all()

        if not components:
            return jsonify({"message" : "No sensors found for this Hydroponic System"}), 404

        sensors_readings = []
        for component in components:
            sensor = Sensor.query.filter_by(id=component.sensor_id).first()
            if not sensor:
                continue 

            readings = []
            sensor_readings = SensorReading.query.filter_by(sensor_id=sensor.id).all()

            for sensor_reading in sensor_readings:
                read = Read.query.filter_by(id=sensor_reading.read_id).first()
                if read:
                    readings.append({
                        "read_id": read.id,
                        "timestamp": read.timestamp,
                        "value": read.value,
                        "createdAt": read.createdAt,
                        "updatedAt": read.updatedAt
                    })

            sensors_readings.append({
                "sensor_id": sensor.id,
                "type": sensor.type,
                "readings": readings
            })

        return jsonify({
            "hydroponic_system_id": hydro_id,
            "sensors": sensors_readings
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)})
