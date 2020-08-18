from threading import Thread
from app.sumo.traci.TraciServer import TraciServer

class TraciStarterThread(Thread):
    traci_server = None
    seconds_since_midnight = 0
    fcm_token = ""

    def __init__(self, seconds_since_midnight, fcm_token):
        Thread.__init__(self)
        self.traci_server = TraciServer()
        self.seconds_since_midnight = seconds_since_midnight
        self.fcm_token = fcm_token


    def run(self):
        print("TRACI STARTER THREAD STARTED!")
        
        self.traci_server.start(self.seconds_since_midnight, self.fcm_token)

        print("TRACI STARTER THREAD STOPPED!")
        
