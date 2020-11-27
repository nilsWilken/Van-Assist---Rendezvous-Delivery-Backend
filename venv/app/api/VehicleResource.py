import threading
import json
import sys
from app.config.firebase import FirebaseCloudMessaging
from app.config.firebase.FirebaseCloudMessaging import CloudMessage

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

from app.config.vehicle_simulation import vehicle_simulation_config

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


@app.route('/api/v1/fleet/vehicle/drivetopos', methods=['PUT'])
def setDriveTopPos():
    TraciHandler.driveToNextParkingAreaWasCalled = True
    print(request.data)
    json_content = json.loads(request.data)
    newVehicleParkingLat = json_content['destination']['lat']
    newVehicleParkingLon = json_content['destination']['lon']
    paResponse = setNewParkingPosLatLon(newVehicleParkingLat, newVehicleParkingLon)
    response = Response(HttpStatus.CREATED, "", paResponse)
    return jsonify(response.serialize())


@app.route('/vehicle/parkingArea/getNext', methods=['GET'])
def getNextParkingArea():
    result = ParkingAreaService.getNextParkingArea()
    response = Response(HttpStatus.OK, "", {"next_parking_area": result})
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/getCurrentState', methods=['GET'])
def get_current_vehicle_state():
    (lat, lon) = traciServer.get_current_van_position()
    is_parking = TraciHandler.driveToNextParkingAreaWasCalled
    door_status = traciServer.get_vehicle_door_status()
    logistic_status = traciServer.get_vehicle_status()
    problem_status = traciServer.get_vehicle_problem_status()
    problem_message = traciServer.get_vehicle_problem_message()

    result = {"latitude": lat, "longitude": lon, "is_parking": is_parking,
                "door_status": door_status, "logistic_status": logistic_status,
                "problem_status": problem_status, "problem_message": problem_message}

    response = Response(HttpStatus.OK, "", result)
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/currpos', methods=['GET'])
def get_current_position():
    (lat, lon) = traciServer.get_current_van_position()
    result = {"lat": lat, "lon": lon}
    response = Response(HttpStatus.OK, "", {"position": result})
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/currtargetpos', methods=['GET'])
def get_current_target_position():
    current_target_position = traciServer.get_current_target_position()
    if current_target_position != None:
        result = {"lat": current_target_position["lat"], "lon": current_target_position["long"]}
    else:
        result = {"lat": 0.0, "lon": 0.0}
    response = Response(HttpStatus.OK, "", {"destination": result})
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/setDoorStatus', methods=['PUT'])
def set_vehicle_door_status():
    json_content = json.loads(request.data)
    door_status = json_content['door_status']

    traciServer = TraciServer()
    traciServer.set_vehicle_door_status(door_status)

    response = Response(HttpStatus.OK, "", None)
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/status', methods=['GET', 'PUT'])
def handle_status():
    if request.method == "GET":
        current_vehicle_status = traciServer.get_vehicle_status()
        response = Response(HttpStatus.OK, "", {"status": current_vehicle_status})
        return jsonify(response.serialize())

    elif request.method == "PUT":
        vehicle_status = request.json["status"]
        traciServer.set_vehicle_status(vehicle_status)
        response = Response(HttpStatus.OK, "", None)
        return jsonify(response.serialize())

@app.route('/api/v1/fleet/vehicle/statectrl', methods=['GET', 'PUT'])
def handle_status_v2():
    if request.method == "GET":
        current_vehicle_status = traciServer.get_vehicle_status()
        response = Response(HttpStatus.OK, "", {"status": current_vehicle_status})
        return jsonify(response.serialize())

    elif request.method == "PUT":
        print("STATECTRL CALLED")
        print(request.data)
        json_content = json.loads(request.data)
        vehicle_status = json_content["vehicle_status"]
        traciServer.set_vehicle_status(vehicle_status)
        response = Response(HttpStatus.OK, "", None)
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


""" ROUTES FOR TESTING PURPOSES """
@app.route('/api/v1/fleet/vehicle/exampleID/currpos', methods=['PUT'])
def test_currpos():
    print("RECEIVED CURRENT POS: " + str(json.loads(request.data)))
    response = Response(HttpStatus.OK, "", None)
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/exampleID/currtargetpos', methods=['PUT'])
def test_currtargetpos():
    print("RECEIVED CURRENT TARGET POS: " + str(json.loads(request.data)))
    response = Response(HttpStatus.OK, "", None)
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/exampleID/status', methods=['PUT'])
def test_status():
    print("RECEIVED CURRENT STATUS: " + str(json.loads(request.data)))
    response = Response(HttpStatus.OK, "", None)
    return jsonify(response.serialize())

@app.route('/api/v1/fleet/vehicle/exampleID/sendProblem', methods=['PUT'])
def test_send_problem():
    traciServer = TraciServer()
    json_content = json.loads(request.data)
    problem_message = json_content['problem_message']
    (lat, lon) = traciServer.get_current_van_position()
    FirebaseCloudMessaging.sendVanProblem(CloudMessage.VAN_PROBLEM, problem_message, str(lat), str(lon))

    traciServer = TraciServer()
    traciServer.set_vehicle_problem_status("PROBLEM")
    traciServer.set_vehicle_problem_message(problem_message)
    
    response = Response(HttpStatus.OK, "", None)
    return jsonify(response.serialize())


@app.route('/api/v1/fleet/vehicle/exampleID/currentProblemSolved', methods=['PUT'])
def test_current_problem_solved():
    traciServer = TraciServer()
    traciServer.set_vehicle_problem_message("")
    traciServer.set_vehicle_problem_status("OK")

    response = Response(HttpStatus.OK, "", None)
    return jsonify(response.serialize())


"""Posts the new parking area to traci"""
def setNewParkingPos(paID, edge):
    result = traciServer.setNewParkPos(paID, edge)
    return result


def setNewParkingPosLatLon(latitude, longitude):
    result = traciServer.setNewParkingPosLatLon(latitude, longitude)
    return result

