from database import db 

class Optimal(db.Model):
    __tablename__ = 'optimals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String)
    min = db.Column(db.Float)
    max = db.Column(db.Float)