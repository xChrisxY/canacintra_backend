from database import db

class Components(db.Model):
    __tablename__ = 'components'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sensor_id = db.Column(db.String, db.ForeignKey('sensors.id'))
    actuator_id = db.Column(db.String)
    hydroponic_system_id = db.Column(db.String, db.ForeignKey('hydroponic_systems.id'))

    sensor = db.relationship('Sensor', backref='components')
    hydroponic_system = db.relationship('HydroponicSystem', backref='components')

