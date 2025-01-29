from database import db 

class SensorReading(db.Model):
    __tablename__ = 'sensor_readings'

    sensor_id = db.Column(db.String, db.ForeignKey('sensors.id'), primary_key=True)
    read_id = db.Column(db.String, db.ForeignKey('reads.id'), primary_key=True)

    sensor = db.relationship('Sensor', backref='readings')
    read = db.relationship('Read', backref='sensors')