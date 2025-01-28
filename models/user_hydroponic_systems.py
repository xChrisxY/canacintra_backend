from database import db

class UserHydroponicSystem(db.Model):
    __tablename__ = 'user_hydroponic_systems'

    user_id = db.Column(db.String, db.ForeignKey('users.id'), primary_key=True)
    hydroponic_system_id = db.Column(db.String, db.ForeignKey('hydroponic_systems.id'), primary_key=True)