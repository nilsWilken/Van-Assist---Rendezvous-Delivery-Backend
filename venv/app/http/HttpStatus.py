class HttpStatus:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    PARKED = 205
    DRIVING = 206
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    UNSUPPORTED_MEDIA_TYPE = 415
    I_AM_A_TEAPOT = 418
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    NETWORK_AUTHENTICATION_REQUIRED = 511

"""Predefined HTTP Status Messages that can be used to build a uniform repsonse"""
class HttpStatusMessage:
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NO_CONTENT = "No Content"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "Not Found"
    METHOD_NOT_ALLOWED = "Method Not Allowed"
    UNSUPPORTED_MEDIA_TYPE = "Unsupported Media Type"
    I_AM_A_TEAPOT = "I am a teapot"
    INTERNAL_SERVER_ERROR = "Internal Server Error"
    NOT_IMPLEMENTED = "Not Implemented"
    NETWORK_AUTHENTICATION_REQUIRED = "Network authentication required"