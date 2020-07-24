from app.database.entity.ParcelEntity import Parcel
from app.database.entity.DeliveryEntity import Delivery
from app.database.entity.CourierEntity import Courier
from app.database.service import CourierService
from app.database.service import ParcelService
from sqlalchemy import update
from app.config.ParcelStatus import ParcelStatus
from app.config.sql_alchemy_conf  import db
import uuid

"""Fetches Delivery Information by ParcelId"""
def getDeliveryByParcelId(parcel_id):
    return Delivery.query.get(parcel_id)


"""Fetches List containing all Delivery Information"""
def getDeliveryListByCourierId(courier_id):
    return db.session.query(Delivery).filter(Delivery.courier_id == courier_id).all()


"""Changes the parcel delivery order"""
def changeParcelDeliveryOrder(courier_id, parcel_id, new_position):
    delivery = getDeliveryByParcelId(parcel_id)
    parcel = ParcelService.getParcel(parcel_id)
    if (delivery != None) & (parcel != None) :
        old_position = delivery.parcel_delivery_position
        delivery_list = getDeliveryListByCourierId(courier_id)

        if int(new_position) >= 0 and int(old_position >= 0) and (int(new_position) != int(old_position)):
            difference = int(new_position) - int(old_position)
            upper_limit = int(new_position)
            lower_limit = int(old_position)

            if difference < 0:
                upper_limit = int(old_position)
                lower_limit = int(new_position)

            ranged_delivery_list = getDeliveryListInRange(delivery_list, lower_limit, upper_limit)
            ranged_delivery_list = changePosition(ranged_delivery_list, int(old_position), int(new_position))
            parcel.verification_token = str(uuid.uuid4())
            db.session.commit()
            return ranged_delivery_list
        return None
    else:
        return None



"""This method is part of the Delivery order change"""
def getDeliveryListInRange(delivery_list, lower_limit, upper_limit):
    new_delivery_list = []
    for delivery in delivery_list:
        if (delivery.parcel_delivery_position >= lower_limit) & (delivery.parcel_delivery_position <= upper_limit):
            new_delivery_list.append(delivery)
    return new_delivery_list


"""This method is part of the Delivery order change"""
def changePosition(delivery_list, old_position, new_position):
    if old_position > new_position:
        for delivery in delivery_list:
            if delivery.parcel_delivery_position == old_position:
                delivery.parcel_delivery_position = new_position
            else:
                delivery.parcel_delivery_position += 1

    elif new_position > old_position:
        for delivery in delivery_list:
            if delivery.parcel_delivery_position == old_position:
                delivery.parcel_delivery_position = new_position
            else: delivery.parcel_delivery_position -= 1
    return delivery_list









