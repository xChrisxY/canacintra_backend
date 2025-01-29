from database import db 
from datetime import datetime

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.String, db.ForeignKey('plant_categories.id'), nullable=False)
    hydroponic_system_id = db.Column(db.String, db.ForeignKey('hydroponic_systems.id'), nullable=False)
    status = db.Column(db.String)
    estimated_harvest = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    category = db.relationship('PlantCategory', backref='plants')
    hydroponic_system = db.relationship('HydroponicSystem', backref='plants')
