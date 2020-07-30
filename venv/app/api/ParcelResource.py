from app import app
from flask import Flask, jsonify, request
from app.http.Response import Response, ResponseMessage
from app.http.HttpStatus import HttpStatus, HttpStatusMessage
from app.database.service import ParcelService
from app.config.firebase import Authentication
from app.database.service import CourierService
from app.database.service import DeliveryService


"""API Definition for Parcel specific data manipulation """
"""" Header: uid, courier_id, verification_token """
@app.route('/parcel/all', methods=['GET'])
def getAllParcel():
    """API Definition for Vehicle specific data manipulation """
    courierValidationResponse = Authentication.checkUserAuthentication(request)
    if courierValidationResponse.status != HttpStatus.OK:
        return jsonify(courierValidationResponse.serialize())
    else:
        courierId = request.headers.get('courier_id')
        verificationToken = request.headers.get('verification_token')
        if ParcelService.doVerificationTokenMatch(courierId, verificationToken) == True:
            response = {'parcel_list':[], 'verification_token':verificationToken}
            return jsonify(Response(HttpStatus.OK, HttpStatusMessage.OK, response).serialize())
        else:
            parcelListWithOrder = ParcelService.getParcelListByCourierId(courierId)
            response = Response(HttpStatus.OK, HttpStatusMessage.OK, parcelListWithOrder)
            return jsonify(response.serialize())


""" Header: uid, courier_id """
""" Body: parcel_id """
@app.route('/parcel/delivery/success', methods=['PUT'])
def confirmParcelDeliverySuccess():
    """API Definition for Vehicle specific data manipulation """
    courierValidationResponse = Authentication.checkUserAuthentication(request)
    if courierValidationResponse.status != HttpStatus.OK:
        return jsonify(courierValidationResponse.serialize())
    else:
        courierId = request.headers.get('courier_id')
        parcel_id  = request.json['parcel_id']
        parcel = ParcelService.confirmParcelDeliverySuccess(parcel_id)
        if parcel == None:
            response = ResponseMessage.PARCEL_NOT_FOUND
        else:
            delivery = DeliveryService.getDeliveryByParcelId(parcel.id)
            response = Response(HttpStatus.OK, HttpStatusMessage.OK, parcel.serializeWithPosition(delivery.parcel_delivery_position))
        return jsonify(response.serialize())


""" Header: uid, courier_id """
""" Body: parcel_id """
@app.route('/parcel/delivery/failure', methods=['PUT'])
def confirmParcelDeliveryFailure():
    """API Definition for Vehicle specific data manipulation """
    courierValidationResponse = Authentication.checkUserAuthentication(request)
    if courierValidationResponse.status != HttpStatus.OK:
        return jsonify(courierValidationResponse.serialize())
    else:
        parcel_id  = request.json['parcel_id']
        parcel = ParcelService.confirmParcelDeliveryFailure(parcel_id)
        if parcel == None:
            response = ResponseMessage.PARCEL_NOT_FOUND
        else:
            delivery = DeliveryService.getDeliveryByParcelId(parcel.id)
            response = Response(HttpStatus.OK, HttpStatusMessage.OK , parcel.serializeWithPosition(delivery.parcel_delivery_position))
        return jsonify(response.serialize())


""" Header: uid, courier_id """
""" Body: parcel_id """
@app.route('/parcel/delivery/undo', methods=['PUT'])
def undoParcelDeliveryConfirmation():
    """API Definition for Vehicle specific data manipulation """
    courierValidationResponse = Authentication.checkUserAuthentication(request)
    if courierValidationResponse.status != HttpStatus.OK:
        return jsonify(courierValidationResponse.serialize())
    else:
        parcel_id  = request.json['parcel_id']
        parcel = ParcelService.undoParcelDeliveryConfirmation(parcel_id)
        if parcel == None:
            response = ResponseMessage.PARCEL_NOT_FOUND
        else:
            delivery = DeliveryService.getDeliveryByParcelId(parcel.id)
            response = Response(HttpStatus.OK, HttpStatusMessage.OK, parcel.serializeWithPosition(delivery.parcel_delivery_position))
        return jsonify(response.serialize())


""" Header: uid, courier_id """
""" Body: parcel_id, new_position """
@app.route('/parcel/order', methods=['PUT'])
def updateParcelOrder():
    """API Definition for Vehicle specific data manipulation """
    ourier_validation_response = Authentication.checkUserAuthentication(request)
    if ourier_validation_response.status != HttpStatus.OK:
        return jsonify(ourier_validation_response.serialize())
    else:
        courier_id = request.headers.get('courier_id')
        parcel_id  = request.json['parcel_id']
        new_position = request.json['new_position']
        delivery_list = DeliveryService.changeParcelDeliveryOrder(courier_id, parcel_id, new_position)
        if delivery_list != None:
            parcel_list = ParcelService.getParcelListByDeliveryList(delivery_list)
            response = Response(HttpStatus.OK, HttpStatusMessage.OK, parcel_list)
            return jsonify(response.serialize())
        return jsonify(ResponseMessage.NOT_POSSIBLE_TO_CHANGE_POSITION.serialize())


"""" Header: uid """
@app.route('/parcel/reset', methods=['GET'])
def resetParcel():
    ParcelService.resetParcelState()
    CourierService.updateAllVerificationToken()
    return "reset successful"


@app.route('/parcel/resetByID', methods=['GET'])
def resetParcelById():
    courierId = request.headers.get('courier_id')
    ParcelService.resetParcelStateById(courierId)
    CourierService.updateVerificationTokenById(courierId)
    return "reset for courier with id " + str(courierId) + " was successfull!"


