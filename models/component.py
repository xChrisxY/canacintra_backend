from database import db
from datetime import datetime

class Component(db.Model):
    __tablename__ = 'components'

    id = db.Column(db.String, primary_key=True)
    hidroponic_system_id = db.Column(db.String, db.ForeignKey('hydroponic_systems.id'))
    plant_id = db.Column(db.String, db.ForeignKey('plants.id'))
    sensor_id = db.Column(db.String, db.ForeignKey('sensors.id'))
    actuator_id = db.Column(db.String, nullable=True)

