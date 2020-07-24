from flask import jsonify
from app.config.sql_alchemy_conf import *
import time
import json

class ParkingArea(db.Model):
    __tablename__ = 'parkingAreas'
    id = db.Column('id', db.Unicode, primary_key=True)
    address = db.Column("address", db.Unicode)
    latitude = db.Column("latitude", db.Unicode)
    longitude = db.Column("longitude", db.Unicode)


    def __init__(self, id, address, latitude, longitude):
        self.id = id
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    