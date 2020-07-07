from app import app
from flask import Flask, jsonify, request
from app.http.Response import Response, ResponseMessage
from app.http.HttpStatus import HttpStatus, HttpStatusMessage
from app.database.service import StopsService
from app.config.firebase import Authentication


@app.route('/stops/all', methods=['GET'])
def get_all_parking_areas():
    parking_area_list = StopsService.getParkingAreaList()
    response = Response(HttpStatus.OK, HttpStatusMessage.OK, parking_area_list)
    return jsonify(response.serialize())