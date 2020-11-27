import json
from app.vehicle_simulation_service.connection import connection
from app.config.vehicle_simulation import vehicle_simulation_config

class simulation_service:

    server_conn = None


    def __init__(self, server_ip, port):
        self.server_conn = connection(server_ip, port)

    
    def authenticate(self):
        #content = {"username": vehicle_simulation_config.VEHICLE_USERNAME, "password": vehicle_simulation_config.VEHICLE_PASSWORD}
        content = {"_id":2,
               "_position":[75,15,86],
               "_destination":[53,43,33],
               "_door":[[5,5],[4,4],[3,3]],
               "_sensors":[1,1,1],
               "_sensors_status":["enable","enable","enable"],
               "_vehicle_status":"INTERVENTION"
               }
        content_json = json.dumps(content)


        response = self.server_conn.send_request_to_server("POST", "/api/v1/security/authenticate", t_body=content_json)
        response_content = response.read()

        # Print response
        print(response_content)

    
    def send_current_position(self, vehicle_id, current_lat, current_lon):
        #position = {"lat": current_lat, "lon": current_lon}
        position = [current_lat, current_lon, 0]
        content = {"position": position}
        content_json = json.dumps(content)
        
        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/currpos"

        response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
        response_content = response.read()

        # Print response
        print(response_content)


    def send_current_target_position(self, vehicle_id, current_target_lat, current_target_lon):
        #destination = {"lat": current_target_lat, "lon": current_target_lon}
        destination = [current_target_lat, current_target_lon, 0]
        content = {"destination": destination}
        content_json = json.dumps(content)

        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/currtargetpos"

        response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
        response_content = response.read()

        # Print response
        print(response_content)


    def send_current_vehicle_status(self, vehicle_id, status):
        content = {"status": status}
        content_json = json.dumps(content)

        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/status"

        response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
        response_content = response.read()

        # Print response
        print(response_content)



    def send_position_reached(self, vehicle_id, current_target_lat, current_target_lon):
        #position = {"lat": current_target_lat, "lon": current_target_lon}
        position = [current_target_lat, current_target_lon, 0]
        content = {"position": position}
        content_json = json.dumps(content)

        path = "/api/v1/fleet/vehicle/" + vehicle_id + "/posreached"

        response = self.server_conn.send_request_to_server("PUT", path, t_body=content_json)
        response_content = response.read()

        # Print response
        print(response_content)
