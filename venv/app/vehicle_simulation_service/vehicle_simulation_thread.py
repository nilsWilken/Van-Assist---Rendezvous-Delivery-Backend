from threading import Thread
from app.vehicle_simulation_service.simulation_service import simulation_service
from app.config.vehicle_simulation import vehicle_simulation_config
import time
from app.sumo.traci.TraciServer import TraciServer

class vehicle_simulation_thread(Thread):
    sim_service = None
    stop = False
    traci_server = None

    def __init__(self):
        Thread.__init__(self)
        self.sim_service = simulation_service(vehicle_simulation_config.SERVER_IP, vehicle_simulation_config.SERVER_PORT)
        self.traci_server = TraciServer()


    def run(self):
        while not self.stop:
            (current_lat, current_lon) = self.traci_server.get_current_van_position()
            self.sim_service.send_current_position(vehicle_simulation_config.VEHICLE_ID, current_lat, current_lon)

            current_target = self.traci_server.get_current_target_position()
            if current_target != None:
                self.sim_service.send_current_target_position(vehicle_simulation_config.VEHICLE_ID, current_target["lat"], current_target["long"])
            else:
                self.sim_service.send_current_target_position(vehicle_simulation_config.VEHICLE_ID, 0.0, 0.0)

            status = self.traci_server.get_vehicle_status()
            self.sim_service.send_current_vehicle_status(vehicle_simulation_config.VEHICLE_ID, status)
            
            time.sleep(vehicle_simulation_config.NOTIFY_INTERVAL)
            

    def request_stop(self):
        self.stop = True
