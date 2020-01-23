from app.http.HttpStatus import HttpStatus, HttpStatusMessage
class Response:
    status = HttpStatus.I_AM_A_TEAPOT
    message = "The server refuses the attempt to brew coffee with a teapot."
    data = None

    def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.data = data

    def serialize(self):
        return {
            'status':self.status,
            'message':self.message,
            'data':self.data
        }


"""Already predefined Reponses --> they just need to be added as a response. No need to build the response every time"""
class ResponseMessage:
    OK = Response(HttpStatus.OK, HttpStatusMessage.OK, None)
    CREATED = Response(HttpStatus.CREATED, HttpStatusMessage.CREATED, None)
    ACCEPTED = Response(HttpStatus.ACCEPTED, HttpStatusMessage.ACCEPTED, None)
    NO_CONTENT = Response(HttpStatus.NO_CONTENT, HttpStatusMessage.NO_CONTENT, None)
    FORBIDDEN = Response(HttpStatus.FORBIDDEN, HttpStatusMessage.FORBIDDEN, None)
    NOT_FOUND = Response(HttpStatus.NOT_FOUND, HttpStatusMessage.NOT_FOUND, None)
    METHOD_NOT_ALLOWED =Response(HttpStatus.METHOD_NOT_ALLOWED, HttpStatusMessage.METHOD_NOT_ALLOWED, None)
    UNSUPPORTED_MEDIA_TYPE = Response(HttpStatus.UNSUPPORTED_MEDIA_TYPE, HttpStatusMessage.UNSUPPORTED_MEDIA_TYPE, None)
    I_AM_A_TEAPOT = Response(HttpStatus.I_AM_A_TEAPOT, HttpStatusMessage.I_AM_A_TEAPOT, None)
    INTERNAL_SERVER_ERROR = Response(HttpStatus.INTERNAL_SERVER_ERROR, HttpStatusMessage.INTERNAL_SERVER_ERROR, None)
    NOT_IMPLEMENTED = Response(HttpStatus.NOT_IMPLEMENTED, HttpStatusMessage.NOT_IMPLEMENTED, None)
    NETWORK_AUTHENTICATION_REQUIRED = Response(HttpStatus.NETWORK_AUTHENTICATION_REQUIRED, HttpStatusMessage.NETWORK_AUTHENTICATION_REQUIRED, None)
    COURIER_ID_VERIFICATION_FAILED = Response(HttpStatus.NOT_FOUND, "courier_id incorrect", None)
    AUTHENTICATION_FAILED = Response(HttpStatus.NETWORK_AUTHENTICATION_REQUIRED, "uid incorrect", None)
    PARCEL_NOT_FOUND = Response(HttpStatus.NOT_FOUND, "parcel_id incorrect", None)
    NOT_POSSIBLE_TO_CHANGE_POSITION = Response(HttpStatus.NOT_FOUND, "not possible to change parcel operation", None)
    SIMULATION_ALREADY_STARTED = Response(HttpStatus.OK, "simulation is already running", None)
    SIMULATION_IS_RUNNING = Response(HttpStatus.OK, "simulation is running", {"simulation_is_running":True})
    SIMULATION_IS_NOT_RUNNING = Response(HttpStatus.OK, "simulation is not running", {"simulation_is_running":False})
    PARING_AREAS_ARE_LOADING = Response(HttpStatus.OK, "Parking areas are already loading", None)
