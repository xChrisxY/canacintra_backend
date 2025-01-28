from database import db 
from datetime import datetime

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.String, primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('plant_categories.id'))
    status = db.Column(db.String, nullable=False)
    planted = db.Column(db.Date, nullable=True)
    estimated_harvest = db.Column(db.Date, nullable=True)
    actual_harvest = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)