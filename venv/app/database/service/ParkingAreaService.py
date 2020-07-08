from app.database.entity.ParkingAreaEntity import ParkingArea
from app.sql_alchemy_conf import db
from sqlalchemy import update


def getParkingAreaList():
    parking_areas = db.session.query(ParkingArea).all()
    result_list = []

    for parking_area in parking_areas:
        result_list.append(parking_area.serialize())

    response = {"parking_area_list": result_list}

    return response


def getParkingArea(id):
    parking_area = ParkingArea.query.get(id)
    return parking_area


def getNextParkingArea():
    #TODO: Implement logic to determine next parking area
    return getParkingArea('hd_0').serialize()



