import firebase_admin
from firebase_admin import messaging
from firebase_admin import _messaging_utils


"""Sends the Silent Push Notification using Firebase"""
def sendMessage(fcm_token, name):
    message = messaging.Message(
        data={
            'name': name
        },
        token=fcm_token
    )
    response = messaging.send(message)
    print('Successfull send message:', response)


"""Sends the Silent Push Notification using Firebase including geo coordinates"""
def sendCurrentPosition(fcm_token, name, latitude, longitude):
    message = messaging.Message(
        data={
            'name': name,
            'latitude': str(latitude),
            'longitude': str(longitude)
        },
        token=fcm_token
    )
    response = messaging.send(message)
    print('Successfull send message:', response)

def sendCurrentDoorStatus(name, door_status):
    message = messaging.Message(
        data={
            'name': name,
            'door_status': door_status
        },
        token=CloudMessage.FCM_TOKEN
    )
    response = messaging.send(message)
    print('Successfull send message:', response)


def sendVanProblem(name, problem_message, latitude, longitude):
    print("FCM Token: ", CloudMessage.FCM_TOKEN)
    message = messaging.Message(
        data={
            'name': name,
            'problem_message': problem_message,
            'latitude': str(latitude),
            'longitude': str(longitude)
        },
        token=CloudMessage.FCM_TOKEN
    )
    response = messaging.send(message)
    print('Successfull send message:', response)


def sendVanLogisticStatus(name, logistic_status):
    message = messaging.Message(
        data={
            'name': name,
            'logistic_status': logistic_status
        },
        token=CloudMessage.FCM_TOKEN
    )
    response = messaging.send(message)
    print('Successfull send message:', response)


"""Predefined cloud messages which are then cached by the mobile app"""
class CloudMessage:
    FCM_TOKEN = ""

    SIMULATION_START = 'simulation_start'
    SIMULATION_STOP = 'simulation_stop'
    VEHICLE_IS_IN_NEXT_PARKING_AREA = 'vehicle_is_in_next_parking_area'
    CURRENT_VAN_LOCATION = 'current_van_location'
    VAN_PROBLEM = 'van_problem'
    DOOR_STATUS = "door_status"
    LOGISTIC_STATUS = "logistic_status"