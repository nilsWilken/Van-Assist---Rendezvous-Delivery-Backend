from flask import jsonify
from app.sql_alchemy_conf import *
import time
import json

class Stop(db.Model):
    __tablename__ = 'stops'
    id = db.Column('id', db.Unicode, primary_key=True)
    adress = db.Column("adress", db.Unicode)
    latitude = db.Column("latitude", db.Unicode)
    longitude = db.Column("longitude", db.Unicode)


    def __init__(self, id, adress, latitude, longitude):
        self.id = id
        self.adress = adress
        self.latitude = latitude
        self.longitude = longitude


    def serialize(self):
        return {
            'id': self.id,
            'adress': self.adress,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    