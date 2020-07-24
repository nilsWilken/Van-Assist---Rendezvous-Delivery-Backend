import http.client
import json

class connection:

    server_ip = None
    port = None

    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port


    def connect_to_server(self):
        return http.client.HTTPConnection(self.server_ip, self.port)


    def send_request_to_server(self, method, path, t_body=None, t_header=None):
        conn = self.connect_to_server()
        if t_body != None and t_header != None:
            conn.request(method, path, headers=header, body=body)
        elif t_body == None:
            conn.request(method, path, headers=header)
        elif t_header == None:
            conn.request(method, path, body=t_body)
        else:
            conn.request(method, path)

        response = conn.getresponse()
        return response
    

