from app import app
from flask import Flask, jsonify, request
from app.http.Response import Response, ResponseMessage
from app.http.HttpStatus import HttpStatus, HttpStatusMessage
from app.database.service import CourierService
from app.sumo.traci.TraciServer import TraciServer
from app.config.firebase import Authentication
from app.sumo.traci import TraciHandler
from app.sumo.traci.TraciStarterThread import TraciStarterThread
import firebase_admin
from firebase_admin import messaging
from firebase_admin import _messaging_utils
import threading


"""" Header: uid, user_name """
@app.route('/courier', methods=['GET'])
def getCourierInformation():
    if Authentication.isAuthenticated(request) == False:
        return jsonify(ResponseMessage.NETWORK_AUTHENTICATION_REQUIRED.serialize())
    else:
        print(request.headers)
        print(request.data)
        userName = request.headers.get('user_name')
        courier = CourierService.getCourierByUserName(userName)
        if courier == None:
            response = ResponseMessage.NOT_FOUND
        else:
            response = Response(HttpStatus.OK, "", courier.serialize())
        return jsonify(response.serialize())


""" Header: uid, courier_id """
""" Body: language_code """
@app.route('/courier/language', methods=['PUT'])
def changeLanguage():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courier_id = request.headers.get('courier_id')
        language_code = request.json['language_code']
        courier = CourierService.changeLanguage(courier_id, language_code)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


def startTraci(seconds_since_midnight, fcm_token):
    traciServer = TraciServer()
    #traciServer.start(seconds_since_midnight, fcm_token)
    traciStarter = TraciStarterThread(seconds_since_midnight, fcm_token)
    traciStarter.start()
    

"""" Header: uid, courier_id, start_time_in_seconds """
@app.route('/courier/day/start', methods=['GET'])
def startDay():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    elif TraciHandler.simulationIsRunning:
        print("---------------------")
        print("Simulation is running")
        print("---------------------")

        traciServer = TraciServer()
        traciServer.update_fcm_token(request.headers.get('fcm_token'))
        
        return jsonify(ResponseMessage.SIMULATION_IS_RUNNING.serialize())
    else:
        courier_id = request.headers.get('courier_id')
        fcm_token = request.headers.get('fcm_token')
        if TraciHandler.startSimulationWasCalledFirst:
            return jsonify(ResponseMessage.SIMULATION_ALREADY_STARTED.serialize())
        seconds_since_midnight = request.headers.get('seconds_since_midnight')
        TraciHandler.startSimulationWasCalledFirst=True
        startTraci(float(seconds_since_midnight), fcm_token)
        print("Traci started!")
        return jsonify(ResponseMessage.OK.serialize())
    return jsonify(ResponseMessage.NOT_FOUND.serialize())


"""" Header: uid, courier_id """
@app.route('/courier/day/finish', methods=['PUT'])
def finishDay():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        if TraciHandler.simulationIsRunning:
            TraciHandler.stopSimulation = True
            while TraciHandler.simulationIsRunning == True:
                """wait"""
                
            print("---------------------")
            print("Simulation stopped!")
            print("---------------------")
                
            return jsonify(ResponseMessage.OK.serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/darkmode/enable', methods=['PUT'])
def enableDarkMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableDarkMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/darkmode/disable', methods=['PUT'])
def disableDarkMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableDarkMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/help_mode/enable', methods=['PUT'])
def enableHelpMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableHelpMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/help_mode/disable', methods=['PUT'])
def disableHelpMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableHelpMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())



@app.route('/courier/notification', methods=['GET'])
def sendCustomNotification():
    registrationToken = request.headers.get('fcm')
    message = messaging.Message(
        data={
            'name':'test_notification'
        },
        token=registrationToken
    )

    response = messaging.send(message)
    print('Successfull send message:', response)
    return jsonify(ResponseMessage.NOT_POSSIBLE_TO_CHANGE_POSITION.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/enable', methods=['PUT'])
def enableAmbientIntelligenceMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableAmbientIntelligenceMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/disable', methods=['PUT'])
def disableAmbientIntelligenceMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableAmbientIntelligenceMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/intelligent_driving_mode/enable', methods=['PUT'])
def enableIntelligentDriving():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableIntelligentDrivingMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/intelligent_driving_mode/disable', methods=['PUT'])
def disableIntelligentDriving():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableIntelligentDrivingMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/time_based_darkmode/enable', methods=['PUT'])
def enableTimeBasedDarkMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableTimeBasedDarkMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/time_based_darkmode/disable', methods=['PUT'])
def disableTimeBasedDarkMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableTimeBasedDarkMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/size_dependent_waiting_mode/enable', methods=['PUT'])
def enableWeightDependentWaiting():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableSizeDependentWaitingMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/size_dependent_waiting_mode/disable', methods=['PUT'])
def disableSizeDependentWaitingMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableSizeDependentWaitingMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())



""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/gamification_mode/enable', methods=['PUT'])
def enableGamificationMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableGamificationMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/gamification_mode/disable', methods=['PUT'])
def disableGamificationMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableGamificationMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/dynamic_content_mode/enable', methods=['PUT'])
def enableDynamicContentMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.enableDynamicContentMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())


""" Header: uid, courier_id """
@app.route('/courier/ambient_intelligence/dynamic_content_mode/disable', methods=['PUT'])
def disableDynamicContentMode():
    courier_validation_response = Authentication.checkUserAuthentication(request)
    if courier_validation_response.status != HttpStatus.OK:
        return jsonify(courier_validation_response.serialize())
    else:
        courierId = request.headers.get('courier_id')
        courier = CourierService.disableDynamicContentMode(courierId)
        if courier != None:
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, courier.serialize()).serialize())
        return jsonify(ResponseMessage.NOT_FOUND.serialize())