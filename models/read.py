from database import db 
from datetime import datetime

class Read(db.Model):
    __tablename__ = 'reads'

    id = db.Column(db.String, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)