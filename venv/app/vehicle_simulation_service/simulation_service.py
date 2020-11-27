import json
from app.vehicle_simulation_service.connection import connection
from app.config.vehicle_simulation import vehicle_simulation_config

class simulation_service:

    server_conn = None
    authenticated = False


    def __init__(self, server_ip, port):
        self.server_conn = connection(server_ip, port)

    def check_authentication(self):
        if not self.authenticated:
            self.authenticate()
    
    def authenticate(self):
        #content = {"username": vehicle_simulation_config.VEHICLE_USERNAME, "password": vehicle_simulation_config.VEHICLE_PASSWORD}
        content = {"_id":2,
               "_position":[75,15,86],
               "_destination":[53,43,33],
               "_door":[[5,5],[4,4],[3,3]],
               "_sensors":[1,1,1],
               "_sensors_status":["enable","enable","enable"],
               "_vehicle_status":"IDLE"
               }
        content_json = json.dumps(content)


        try:
            response = self.server_conn.send_request_to_server("POST", "/api/v1/security/authenticate", t_body=content_json)
            response_content = response.read()

            # Print response
            print("Sucessfully authenticated!")
            print(response_content)
            self.authenticated = True
        except:
            print("Authentication call failed!")

    
    def send_current_position(self, vehicle_id, current_lat, current_lon):
        self.check_authentication()
        #position = {"lat": current_lat, "lon": current_lon}
        position = [current_lat, current_lon, 0]
        content = {"position": position}
        content_json = json.dumps(content)
        
        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/currpos"

        try:
            response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
            response_content = response.read()

            # Print response
            print(response_content)
        except:
            print("Connection refused!")
            self.authenticated = False


    def send_current_target_position(self, vehicle_id, current_target_lat, current_target_lon):
        self.check_authentication()
        #destination = {"lat": current_target_lat, "lon": current_target_lon}
        destination = [current_target_lat, current_target_lon, 0]
        content = {"destination": destination}
        content_json = json.dumps(content)

        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/currtargetpos"

        try:
            response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
            response_content = response.read()

            # Print response
            print(response_content)
        except:
            print("Connection refused!")
            self.authenticated = False


    def send_current_vehicle_status(self, vehicle_id, status):
        self.check_authentication()
        content = {"status": status}
        content_json = json.dumps(content)

        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/drvsysstatus"

        try:
            response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
            response_content = response.read()

            # Print response
            print(response_content)
        except:
            print("Connection refused!")
            self.authenticated = False



    def send_position_reached(self, vehicle_id, current_target_lat, current_target_lon):
        self.check_authentication()
        #position = {"lat": current_target_lat, "lon": current_target_lon}
        position = [current_target_lat, current_target_lon, 0]
        content = {"position": position}
        content_json = json.dumps(content)

        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/posreached"

        try:
            response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
            response_content = response.read()

            print("POSREACHED SENT!")
            # Print response
            print(response)
        except:
            print("Connection refused!")
            self.authenticated = False
