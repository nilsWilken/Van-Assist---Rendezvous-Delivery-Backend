from firebase_admin import auth
from app.database.service import CourierService
from app.http.Response import Response, ResponseMessage
from flask import request

"""Checks if the Firebase Authentication is correct"""
def isAuthenticated(request):
	#return True
    id_token  = request.headers.get('uid')

    if hasWildcard(id_token):
        return True
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return True
    except Exception as e:
        return False


"""Direct access is granted when uid is vanassist19 -> only use for testing"""
def hasWildcard(uid):
    if uid == "vanassist2019":
        return True
    return False


"""Checks if the user is known by the server"""
def checkUserAuthentication(request):
    authSuccessful = isAuthenticated(request)
    if authSuccessful == False:
        return ResponseMessage.AUTHENTICATION_FAILED
    else:
        courier_id = request.headers.get('courier_id')
        if CourierService.validateCourierById(courier_id) == False:
            return ResponseMessage.COURIER_ID_VERIFICATION_FAILED
        else:
            return ResponseMessage.OK



