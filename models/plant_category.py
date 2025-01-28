from database import db
from datetime import datetime

class PlantCategory(db.Model):
    __tablename__ = 'plant_categories'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    harvest_days = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=True)
    group_id = db.Column(db.String, db.ForeignKey('plant_groups.id'))