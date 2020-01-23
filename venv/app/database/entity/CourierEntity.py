from flask import jsonify
from app.sql_alchemy_conf import *
import time
import json

class Courier(db.Model):
    __tablename__ = 'courier'
    id = db.Column('id', db.Unicode, primary_key=True)
    first_name = db.Column('first_name', db.Unicode)
    last_name = db.Column('last_name', db.Unicode)
    user_name = db.Column('user_name', db.Unicode)
    phone_number = db.Column('phone_number', db.Unicode)
    dark_mode = db.Column('dark_mode', db.Integer)
    help_mode = db.Column('help_mode', db.Integer)
    ambient_intelligence_mode = db.Column('ambient_intelligence_mode', db.Integer)
    time_based_dark_mode = db.Column('time_based_dark_mode', db.Integer)
    intelligent_driving_mode = db.Column('intelligent_driving_mode', db.Integer)
    size_dependent_waiting_mode = db.Column('size_dependent_waiting_mode', db.Integer)
    dynamic_content_mode = db.Column('dynamic_content_mode', db.Integer)
    gamification_mode = db.Column('gamification_mode', db.Integer)
    language_code = db.Column('language_code', db.Unicode)
    verification_token = db.Column('verification_token', db.Unicode)


    def __init__(self, first_name, last_name, user_name, phone_number, dark_mode, help_mode, ambient_intelligence_mode, time_based_dark_mode, intelligent_driving_mode, size_dependent_waiting_mode, gamification_mode, dynamic_content_mode, language_code, verification_token):
        self.id = int(round(time.time() * 1000))
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.dark_mode = dark_mode
        self.help_mode = help_mode
        self.ambient_intelligence_mode = ambient_intelligence_mode
        self.time_based_dark_mode = time_based_dark_mode
        self.intelligent_driving_mode = intelligent_driving_mode
        self.size_dependent_waiting_mode = size_dependent_waiting_mode
        self.gamification_mode = gamification_mode
        self.dynamic_content_mode = dynamic_content_mode
        self.language_code = language_code
        self.verification_token = verification_token

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name':self.last_name,
            'user_name':self.user_name,
            'phone_number':self.phone_number,
            'dark_mode':self.dark_mode,
            'help_mode':self.help_mode,
            'ambient_intelligence_mode':self.ambient_intelligence_mode,
            'time_based_dark_mode':self.time_based_dark_mode,
            'intelligent_driving_mode':self.intelligent_driving_mode,
            'size_dependent_waiting_mode':self.size_dependent_waiting_mode,
            'gamification_mode':self.gamification_mode,
            'dynamic_content_mode':self.dynamic_content_mode,
            'language_code':self.language_code
        }
