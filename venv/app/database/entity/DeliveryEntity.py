from flask import jsonify
from app.database.entity.ParcelEntity import Parcel
from app.config.sql_alchemy_conf import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import ForeignKey
import time
import json

class Delivery(db.Model):
    __tablename__ = 'delivery'
    parcel_id = db.Column('parcel_id', db.Unicode, primary_key=True)
    courier_id = db.Column('courier_id', db.Unicode)
    van_id = db.Column('van_id', db.Unicode)
    parcel_delivery_position = db.Column('parcel_delivery_position', db.Unicode)

    def __init__(self, courier_id, parcelId, van_id, parcel_delivery_position):
        self.courier_id = courier_id
        self.parcelId = parcelId
        self.van_id = van_id
        self.parcel_delivery_position = parcel_delivery_position

    def serialize(self):
        return {
            'courier_id': self.courier_id,
            'parcel_id': self.parcel_id,
            'van_id':self.van_id,
            'parcel_delivery_position':self.parcel_delivery_position
        }
