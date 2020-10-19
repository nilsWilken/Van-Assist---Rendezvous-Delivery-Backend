from flask import Flask
import time, os, sys
#from app.sql_alchemy_conf import db
from app.sumo.traci import TraciHandler
from app.sumo.traci.TraciServer import TraciServer
from app.config import sql_alchemy_conf
from app.vehicle_simulation_service.vehicle_simulation_thread import vehicle_simulation_thread
from app.config.vehicle_simulation import vehicle_simulation_config

print('/> STARTING_FLASK')
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

import firebase_admin
from firebase_admin import credentials

cred_path = os.path.dirname(os.path.realpath(__file__)) + "/config/firebase/vanassist-f4bf3-firebase-adminsdk-vst0l-a8926b77a8.json"

cred = credentials.Certificate(cred_path)

default_app = firebase_admin.initialize_app(cred)

"""The greyed out comment can be used to when connection to a local database on the local machine"""
#dbconnection = 'mysql://root:@localhost:3306/vanassist'
#dbconnection = 'mysql://admin:vanassist@127.0.0.1:3306/vanassist'
#dbconnection = 'mysql://admin:vanassist@134.155.108.94:3306/vanassist'
dbconnection = 'mysql://admin:vanassist@134.155.109.10:3306/vanassist'

app.config['SQLALCHEMY_DATABASE_URI'] = dbconnection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sql_alchemy_conf.db = SQLAlchemy(app)

from app.api import ParcelResource, CourierResource, VehicleResource, ParkingAreaResource

print('DATABASE CONNECTED')

print('STARTED TO LOAD PARKING AREAS')
TraciHandler.parkingAreasAreLoading = True
traciServer = TraciServer()
traciServer.loadParkingAreas()
TraciHandler.parkingAreasAreLoading = False
print('PARKING AREAS LOADED')

if vehicle_simulation_config.START_COMM_SIMULATION_THREAD:
    sim_thread = vehicle_simulation_thread()
    sim_thread.start()









