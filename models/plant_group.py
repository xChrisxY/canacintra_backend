from database import db
from datetime import datetime

class PlantGroup(db.Model):
    __tablename__ = 'plant_groups'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    optimal_temp = db.Column(db.String, db.ForeignKey('optimals.id'))
    optimal_humidity = db.Column(db.String, db.ForeignKey('optimals.id'))
    optimal_ph = db.Column(db.String, db.ForeignKey('optimals.id'))
    optimal_ec = db.Column(db.String, db.ForeignKey('optimals.id'))