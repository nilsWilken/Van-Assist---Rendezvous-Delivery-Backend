import threading

try:
    import queue
except ImportError:
    import Queue as queue

from app import app
from flask import Flask, jsonify, request
from app.http.Response import Response, ResponseMessage
from app.http.HttpStatus import HttpStatus, HttpStatusMessage
from app.database.service import ParcelService
from app.config.firebase import Authentication
from app.Location import Location
from app.sumo.traci import TraciHandler
from app.database.service import ParkingAreaService
import uuid

from app.sumo.traci import TraciHandler
from app.sumo.traci.TraciServer import TraciServer

traciServer = TraciServer()

"""API Definition for Vehicle specific data manipulation """

""" Header: uid, courier_id """
""" Body: vehicle_latitude, vehicle_longitude"""
@app.route('/vehicle/parkingArea/next', methods=['POST'])
def setNextparkingLocation():
    """API Definition for Vehicle specific data manipulation """
    if Authentication.isAuthenticated(request) == False:
        return jsonify(ResponseMessage.NETWORK_AUTHENTICATION_REQUIRED.serialize())
    else:
        TraciHandler.driveToNextParkingAreaWasCalled = True
        newVehicleParkingPos = request.json['parkingArea']['id']
        newVehicleParkingEdge = request.json['parkingArea']['edge']
        paResponse = setNewParkingPos(newVehicleParkingPos, newVehicleParkingEdge)
        response = Response(HttpStatus.CREATED, "", paResponse)
        return jsonify(response.serialize()) 


@app.route('/vehicle/parkingArea/getNext', methods=['GET'])
def getNextParkingArea():
    result = ParkingAreaService.getNextParkingArea()
    response = Response(HttpStatus.OK, "", {"next_parking_area": result})
    return jsonify(response.serialize())


""" Header: uid, courier_id """
@app.route('/vehicle/parkingArea/all', methods=['GET'])
def getAllParkingAreas():
    """API Definition for Vehicle specific data manipulation """
    if Authentication.isAuthenticated(request) == False:
        return jsonify(ResponseMessage.NETWORK_AUTHENTICATION_REQUIRED.serialize())
    elif TraciHandler.parkingAreasAreLoading:
        print("parking aread are loading... ")
        return jsonify(ResponseMessage.PARING_AREAS_ARE_LOADING.serialize())
    else:
        TraciHandler.parkingAreasAreLoading = True
        result = traciServer.returnParkingAreas()
        TraciHandler.parkingAreasAreLoading=False
        response = Response(HttpStatus.OK, "", result)
        return jsonify(response.serialize())

"""Posts the new parking area to traci"""
def setNewParkingPos(paID, edge):
    result = traciServer.setNewParkPos(paID, edge)
    return result

