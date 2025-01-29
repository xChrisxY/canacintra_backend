from database import db
from datetime import datetime

class Sensor(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String, nullable=False)