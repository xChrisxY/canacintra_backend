from database import db
from datetime import datetime

class Sensor(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String, nullable=False)