from datetime import datetime

from weather_recorder import db

class Weather(db.Model):
    reading_id = db.Column(db.Integer, primary_key=True)
    date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    temperature_low = db.Column(db.Integer, nullable=False)
    temperature_high = db.Column(db.Integer, nullable=False)
    wind_kmh = db.Column(db.Integer, nullable=False)
    rainfall_mm = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f"{self.date_taken}, {self.temperature_high}")
