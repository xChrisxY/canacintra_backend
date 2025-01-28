from database import db 
from datetime import datetime

class Optimal(db.Model):
    __tablename__ = 'optimals'

    id = db.Column(db.String, primary_key=True)
    value = db.Column(db.String, nullable=False)
    min = db.Column(db.Float, nullable=False)
    max = db.Column(db.Float, nullable=False)