from flask import jsonify
from app.sql_alchemy_conf import *
import time
import json

class Parcel(db.Model):
    __tablename__ = 'parcel'
    id = db.Column('id', db.Unicode, primary_key=True)
    state = db.Column('state', db.Integer)
    name_of_recipient = db.Column('name_of_recipient', db.Unicode)
    phone_number = db.Column('phone_number', db.Unicode)
    additional_recipient_information = db.Column('additional_recipient_information', db.Unicode)
    latitude = db.Column('latitude', db.Unicode)
    longitude = db.Column('longitude', db.Unicode)
    floor = db.Column('floor', db.Integer)
    city = db.Column('city', db.Unicode)
    address = db.Column('address', db.Unicode)
    additional_address_information = db.Column('additional_address_information', db.Unicode)
    weight = db.Column('weight', db.Float)
    width = db.Column('width', db.Float)
    height = db.Column('height', db.Float)
    length = db.Column('length', db.Float)
    parkingArea = db.Column('parkingArea', db.Unicode)
    verification_token = db.Column('verification_token', db.Unicode)


    def __init__(self, name, state, name_of_recipient, additional_recipient_information, phone_number, latitude, longitude, floor, address, city, additional_address_information, weight, width, height, length, parkingArea, verification_token):
        self.id = int(round(time.time() * 1000))
        self.state = state
        self.name_of_recipient = name_of_recipient
        self.additional_recipient_information = additional_recipient_information
        self.phone_number = phone_number
        self.latitude = latitude
        self.longitude = longitude
        self.floor = floor
        self.city = city
        self.address = address
        self.additional_address_information = additional_recipient_information
        self.weight = weight
        self.width = width
        self.height = height
        self.length = length
        self.parkingArea = parkingArea
        self.verification_token = verification_token

    def serialize(self):

        return {
            'id': self.id,
            'state':self.state,
            'name_of_recipient':self.name_of_recipient,
            'additional_recipient_information':self.additional_recipient_information,
            'phone_number':self.phone_number,
            'latitude':self.latitude,
            'longitude':self.longitude,
            'floor':self.floor,
            'city': self.city,
            'address':self.address,
            'additional_address_information':self.additional_address_information,
            'weight':self.weight,
            'width':self.width,
            'height':self.height,
            'length':self.length,
            'parkingArea': self.parkingArea,
            'verification_token': self.verification_token
        }

    def serializeWithPosition(self, delivery_position):
        parcel_dict = self.serialize()
        parcel_dict["delivery_position"] = delivery_position
        return parcel_dict
