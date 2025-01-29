from database import db

class PlantCategory(db.Model):
    __tablename__ = 'plant_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    harvest_days = db.Column(db.Integer)
    image = db.Column(db.String)
    plant_group_id = db.Column(db.String, db.ForeignKey('plant_groups.id'), nullable=False)

    plant_group = db.relationship('PlantGroup', backref='categories')