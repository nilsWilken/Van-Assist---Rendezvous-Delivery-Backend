import http.client
import ssl
import json
import os
from app.config.vehicle_simulation import vehicle_simulation_config

class connection:

    server_ip = None
    port = None

    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port


    def connect_to_server(self):
        if vehicle_simulation_config.HTTPS_CONNECTION:
            cert_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "certificate/hso_pem_cert.pem")
            key_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "certificate/test.key")

            if not os.path.exists(cert_path):
                print("CERTIFICATE FILE NOT FOUND!")
            
            if not os.path.exists(key_path):
                print("KEY FILE NOT FOUND!")

            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(cert_path, key_path)
            return http.client.HTTPSConnection(self.server_ip, port=self.port, context=ssl_context, timeout=vehicle_simulation_config.CONNECTION_ATTEMPT_TIMEOUT)
        else: 
            return http.client.HTTPConnection(self.server_ip, self.port, timeout=vehicle_simulation_config.CONNECTION_ATTEMPT_TIMEOUT)


    def send_request_to_server(self, method, path, t_body=None, t_header=None):
        conn = self.connect_to_server()
        if t_body != None and t_header != None:
            conn.request(method, path, headers=t_header, body=t_body)
        elif t_body == None:
            conn.request(method, path, headers=t_header)
        elif t_header == None:
            conn.request(method, path, body=t_body)
        else:
            conn.request(method, path)

        response = conn.getresponse()
        return response
    

