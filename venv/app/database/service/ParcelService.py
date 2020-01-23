from app.database.entity.ParcelEntity import Parcel
from app.database.entity.DeliveryEntity import Delivery
from app.database.entity.CourierEntity import Courier
from app.database.service import CourierService
from app.sql_alchemy_conf  import db
from sqlalchemy import update
from app.config.ParcelStatus import ParcelStatus
import uuid


"""Fetches List of all parcel by the courierId"""
def getParcelListByCourierId(courier_id):

    delivery_list = db.session.query(Delivery).filter(Delivery.courier_id == courier_id).all()
    result_list = []
    for delivery in delivery_list:
        parcel = getParcel(delivery.parcel_id)
        if parcel != None:
            result_list.append({
                'id': parcel.id,
                'state': parcel.state,
                'name_of_recipient': parcel.name_of_recipient,
                'phone_number': parcel.phone_number,
                'additional_recipient_information': parcel.additional_recipient_information,
                'latitude': parcel.latitude,
                'longitude': parcel.longitude,
                'address': parcel.address,
                'city':parcel.city,
                'additional_address_information':parcel.additional_address_information,
                'weight': parcel.weight,
                'width': parcel.width,
                'height': parcel.height,
                'length': parcel.length,
                'verification_token': parcel.verification_token,
                'delivery_position':delivery.parcel_delivery_position
            })

    courier = CourierService.getCourierById(courier_id)
    response = {'parcel_list': result_list,
                'verification_token': courier.verification_token}
    return response


"""Fetches all parcel by the delivery list"""
def getParcelListByDeliveryList(delivery_list):
    result_list = []
    for delivery in delivery_list:
        parcel = getParcel(delivery.parcel_id)
        if parcel != None:
            result_list.append({
                'id': parcel.id,
                'state': parcel.state,
                'name_of_recipient': parcel.name_of_recipient,
                'phone_number': parcel.phone_number,
                'additional_recipient_information': parcel.additional_recipient_information,
                'latitude': parcel.latitude,
                'longitude': parcel.longitude,
                'address': parcel.address,
                'city':parcel.city,
                'additional_address_information': parcel.additional_address_information,
                'weight': parcel.weight,
                'width': parcel.width,
                'height': parcel.height,
                'length': parcel.length,
                'verification_token': parcel.verification_token,
                'delivery_position': delivery.parcel_delivery_position
            })
    return result_list


"""Fetches parcel by id"""
def getParcel(id):
    parcel = Parcel.query.get(id)
    return parcel


"""Confirms the successful parcel delivery"""
def confirmParcelDeliverySuccess(id):
    parcel = getParcel(id)
    if parcel != None:
        parcel.state = ParcelStatus.DELIVERY_SUCCESS
        parcel.verification_token = str(uuid.uuid4())
        db.session.commit()
    return parcel


"""Confirms the unsuccessful parcel delivery"""
def confirmParcelDeliveryFailure(id):
    parcel = getParcel(id)
    if parcel != None:
        parcel.state = ParcelStatus.DELIVERY_FAILURE
        parcel.verification_token = str(uuid.uuid4())
        db.session.commit()
    return parcel


"""Confirms the undo of a parcel"""
def undoParcelDeliveryConfirmation(id):
    parcel = getParcel(id)
    if parcel != None:
        parcel.state = ParcelStatus.PLANNED
        parcel.verification_token = str(uuid.uuid4())
        db.session.commit()
    return parcel


"""Checks if the verification token mach (first token was sent in the request, the second is stored on the server"""
def doVerificationTokenMatch(courier_id, verification_token):
    courier = CourierService.getCourierById(courier_id)
    if verification_token == courier.verification_token:
        return True
    else:
        return False


"""Allows to reset the parcel state to planned without needing to log in"""
def resetParcelState():
    parcel_list = db.session.query(Parcel).all()
    for parcel in parcel_list:
        parcel.state = 0
    db.session.commit()

