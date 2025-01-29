from database import db
from datetime import datetime

class PlantGroup(db.Model):
    __tablename__ = 'plant_groups'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    optimal_temp_id = db.Column(db.String, db.ForeignKey('optimals.id'))
    optimal_humidity_id = db.Column(db.String, db.ForeignKey('optimals.id'))
    optimal_ph_id = db.Column(db.String, db.ForeignKey('optimals.id'))
    optimal_ec_id = db.Column(db.String, db.ForeignKey('optimals.id'))

    optimal_temp = db.relationship('Optimal', foreign_keys=[optimal_temp_id])
    optimal_humidity = db.relationship('Optimal', foreign_keys=[optimal_humidity_id])
    optimal_ph = db.relationship('Optimal', foreign_keys=[optimal_ph_id])
    optimal_ec = db.relationship('Optimal', foreign_keys=[optimal_ec_id])
