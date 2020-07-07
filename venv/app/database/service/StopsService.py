from app.database.entity.StopsEntity import Stop
from app.sql_alchemy_conf import db
from sqlalchemy import update


def getParkingAreaList():
    parking_areas = db.session.query(Stop).all()
    result_list = []

    for parking_area in parking_areas:
        result_list.append(parking_area.serialize())

    response = {"parking_area_list": result_list}

    return response


def getParkingArea(id):
    parking_area = Stop.query.get(id)
    return parking_area



