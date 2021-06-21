from app.database.entity.ParkingAreaEntity import ParkingArea
from app.config.sql_alchemy_conf import db
from sqlalchemy import update
from app.sumo.traci import TraciHandler


nextParkingArea = "H2"


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
    global nextParkingArea
    if nextParkingArea == "H1":
        nextParkingArea = "H2"
    elif nextParkingArea == "H2":
        nextParkingArea = "H3"
    elif nextParkingArea == "H3":
        nextParkingArea = "H4"
    elif nextParkingArea == "H4":
        nextParkingArea = "H5"
    for paArea in TraciHandler.parkingAreaList:
        if paArea["name"] == nextParkingArea:
            return paArea

def resetNextParkingArea():
    global nextParkingArea
    nextParkingArea = "H2"




