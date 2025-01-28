from database import db 
from datetime import datetime

class HydroponicSystem(db.Model):
    __tablename__ = 'hydroponic_systems'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
