import os, sys
import time
import math
from geo.sphere import bearing, destination
from lxml import etree          # used for parsing XML Files
from app.sumo.traci import TraciHandler
from app.config.firebase import FirebaseCloudMessaging
from app.config.firebase.FirebaseCloudMessaging import CloudMessage
from app.sumo.traci.ParkingArea import ParkingArea
import gc
from app.vehicle_simulation_service.simulation_service import simulation_service
from app.config.vehicle_simulation import vehicle_simulation_config

import time

class TraciServer:
    
    VEHICLE_STATES = ["IDLE", "AUTO_DRIVING", "MAN_DRIVING", "PARKING", "WAITING", "DOORS_OPEN", "INTERVENTION", "HARD_FAULT"]
    INTERVENTION_LAT = 49.416761
    INTERVENTION_LON = 8.684942
    FILTER_POSITION_LAT = 49.419171
    FILTER_POSITION_LON = 8.684352

    __instance = None
    step = 0
    checkNewPark = False
    rerouteStarted = False
    checkParkArrivedBool = False
    parkingArrived = False
    nextPaID = ""
    nextPaEdge = ""
    isEnvironmentVariableSet = False
    sumoBinary = ""
    sumoCmd = ""
    hasNewParkingArea = False
    nameOfArea = ""
    accessPath = ""
    routesPath = ""
    routesEtree = ""
    parkingAreaPath = ""
    parkingAreaEtree = ""
    path = None
    net = None
    x_off = 0.0
    y_off = 0.0
    p1 = None
    p2 = None
    current_van_lat_geo = 49.416937
    current_van_long_geo = 8.678421
    vehicle_status = 0
    sim_service = None
    fcm_token = ""
    door_status = "CLOSED"
    problem_status = "OK"
    problem_message = ""


    """SUMP Paths are configures here"""
    def configurePath(self, file):
        self.accessPath =  os.path.dirname(os.path.realpath(__file__)) + "/config/" + file
        return self.accessPath


    def __init__(self):
        self.sim_service = simulation_service(vehicle_simulation_config.SERVER_IP, vehicle_simulation_config.SERVER_PORT)

    """Constructor"""
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


    """SUMP Paths are configures here"""
    def configure(self):
        if 'SUMO_HOME' in os.environ:
            tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
            sys.path.append(tools)
            sumolib = os.path.join(os.environ['SUMO_HOME'], 'tools/sumolib')
            sys.path.append(sumolib)
            self.isEnvironmentVariableSet = True
        else:
            sys.exit("please declare environment variable 'SUMO_HOME'")


    """All available parking areas are loaded form the xml file containing the parkingAreas"""
    def loadParkingAreas(self):
        if(len(TraciHandler.parkingAreaList) == 0):
            self.parkingAreaPath = self.configurePath("parkingAreas.add.xml")
            self.parkingAreaEtree= etree.parse(self.parkingAreaPath)
            paid = self.retrieve_parking_areas()
            paDict = {}
            result_list = []
            counter = 0
            self.configure()
            self.configureGEOfromXY()
            for pa in paid:
                (edge, beg_x, beg_y, end_x, end_y) = self.retrieve_parking_areas_coordinates(pa)
                (name, length, lane, roadsideCap, startPos, endPos) = self.retrieve_parking_areas_vals(pa)
                (lat, long) = self.coordinateTransformationForParkingAreas(beg_x, beg_y, end_x, end_y, length, startPos)

                counter = counter+1
                print(str(counter))

                parkingArea = ParkingArea(id=pa, name = name, lane=lane, edge = edge, length =length, roadsideCap=roadsideCap, startPos=startPos, endPos=endPos, lat = lat, long=long, x=beg_x, y=beg_y)
                #paDict[pa] = parkingArea
                result_list.append({
                'id': parkingArea.id,
                'name': parkingArea.name,
                'length': parkingArea.length,
                'lane':parkingArea.lane,
                'edge':parkingArea.edge,
                'roadsideCapacity':parkingArea.roadsideCapacity,
                'startPos':parkingArea.startPos,
                'endPos':parkingArea.endPos,
                'lat': parkingArea.lat,
                'long': parkingArea.long,
                'x': parkingArea.x,
                'y': parkingArea.y
            })

            TraciHandler.parkingAreaList = result_list
        else:
            print("exist")


    """Coordinates the transoformation from SUMO to GEO Coordiantes for the Parking Areas"""
    def coordinateTransformationForParkingAreas(self, beg_x, beg_y, end_x, end_y, length, startPos):
        # convert SUMO coordinates into GEO Coordinates
        # beginning
        (long1, lat1) = self.convertGEOfromXYWithoutConfiguration(beg_x, beg_y)
        beginning = (lat1, long1)
        # end
        (long2, lat2) = self.convertGEOfromXYWithoutConfiguration(end_x, end_y)
        end = (lat2, long2)
        # use shape beginning and endpoint to retrieve bearing
        bear = bearing(beginning, end)
        # use parkingArea Length and StartPos to calculate distance
        parkStart = float(startPos) + (float(length) / 2)
        # print(parkStart)
        # use destination calculation to calculate final
        return destination(beginning, parkStart, bear)


    def returnParkingAreas(self):
        if(len(TraciHandler.parkingAreaList) == 0):
            self.loadParkingAreas()
            return TraciHandler.parkingAreaList
        else:
            return TraciHandler.parkingAreaList


    #########################################################
    # Parse XML with parkingAreas and get all parkingAreas IDs
    # return: list of parkingIDs
    def retrieve_parking_areas(self):
        strRes = self.parkingAreaEtree.xpath('//parkingArea/@id')
        return strRes

    def retrieve_parking_areas_vals(self,pa):
        parkArea = self.parkingAreaEtree # etree.parse(path)
        path = "//parkingArea[@id='" + pa + "']/@*"
        all = parkArea.xpath(path)
        name = all[1]
        length = all[2]
        lane = all[3]
        roadsideCap = all[4]
        startPos = all[5]
        endPos = all[6]

        return (name, length, lane, roadsideCap, startPos, endPos)


    #########################################################
    # Parse XML with parkingAreas and XML with whole MAP - get the coordinates of each ParkingArea Entry
    # Entry of parkingArea = Starting coordinates of the lane
    # return: coordinates of the ParkingArea Entry (pa)
    def retrieve_parking_areas_coordinates(self,pa):
        path = "//parkingArea[@id='" + pa + "']/@lane"
        la = self.parkingAreaEtree.xpath(path)  # get Lane ID of the parking Area

        path = self.configurePath("Heidelberg_Streetnames.net.xml")
        Map = etree.parse(path)
        path1 = "//net/edge/lane[@id='" + la[0] + "']/@shape"
        shape = Map.xpath(path1)  # get the whole Shape of the Lane
        pathEdge ="//edge/lane[@id='" + la[0] + "']/../@id"
        edge = Map.xpath(pathEdge)
        beginning_coordinates = shape[0].split()  # get the coordinates of the Entry
        [beginning_x, beginning_y] = beginning_coordinates[0].split(",")
        end_coordinates = shape[0].split()  # get the coordinates of the Entry
        [end_x, end_y] = end_coordinates[1].split(",")
        return (edge[0], float(beginning_x), float(beginning_y), float(end_x), float(end_y))





    #########################################################
    # Check if there are empty parking Areas
    # return True - if all parking Areas are full
    # return False - otherwise
    def checkFull(pA):
        boolean = True
        for k, v in pA.items():
            if not v:
                boolean = False
        return boolean


    """Converts SUMO to GEO coordinates --> Therefore it uses the already read xml files"""
    def convertGEOfromXYWithoutConfiguration(self, x, y):
        lon = 0
        lat = 0
        from pyproj import Proj, transform

        x -= self.x_off
        y -= self.y_off
        # copy the SR-ORG:6781 definition in Proj4 format from http://spatialreference.org/ref/sr-org/6781/
        # Transform point (155000.0, 446000.0) with SR-ORG:6781
        lon, lat, z = transform(self.p1, self.p2, x, y, 0.0)
        return (lon, lat)


    """Loads the XML Files"""
    def configureGEOfromXY(self):
        from sumolib import net
        self.path = self.configurePath("Heidelberg_Streetnames.net.xml")
        self.net = net.readNet(self.path)
        from pyproj import Proj, transform
        x_off, y_off = self.net.getLocationOffset()
        self.x_off = x_off
        self.y_off = y_off
        self.p1 = Proj(
            "+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        self.p2 = Proj(proj='latlong', datum='WGS84')


 


    """A new parking area is set in this method """
    def setNewParkPos(self, paID, paEdge):
        self.nextPaID = paID
        for pa in TraciHandler.parkingAreaList:
            if pa["id"] == self.nextPaID:
                returnPA = pa
                print(pa)
                break
        try:
            if (TraciHandler.stopSimulation==False and self.step < 86400):#
                self.nextPaEdge = paEdge
                self.checkNewPark = True
        except:
            print("An exception occurred")
        return returnPA

    def setNewParkingPosLatLon(self, lat, lon):
        #print(len(TraciHandler.parkingAreaList))
        #for pa in TraciHandler.parkingAreaList:
        #    print(str(pa["lat"]) + " " + str(pa["long"]))
        #    if pa["lat"] == lat and pa["long"] == lon:
        #        self.nextPaID = pa["id"]
        #        paEdge = pa["edge"]
        #        returnPA = pa
        #        print(pa)
        #        break
        returnPA = ""
        try:
            if(TraciHandler.stopSimulation == False and TraciHandler.startSimulationWasCalledFirst == True and self.step < 86400):
                returnPA = self.get_closest_parking_area(lat, lon)
                filter_position_pa = self.get_closest_parking_area(TraciServer.FILTER_POSITION_LAT, TraciServer.FILTER_POSITION_LON)
                intervention_pa = self.get_closest_parking_area(TraciServer.INTERVENTION_LAT, TraciServer.INTERVENTION_LON)
                if returnPA["id"] == filter_position_pa["id"]:
                    if self.nextPaID == intervention_pa["id"]:
                        returnPA = filter_position_pa
                    else:
                        returnPA = intervention_pa

                if self.nextPaID is not returnPA["id"] and self.get_vehicle_status() is not "INTERVENTION" and self.get_vehicle_status() is not "HARD_FAULT":
                    self.nextPaID = returnPA["id"]
                    paEdge = returnPA["edge"]
                    self.nextPaEdge = paEdge
                    self.checkNewPark = True
                else:
                    TraciHandler.driveToNextParkingAreaWasCalled=False
                    print("Already located at the closest parking area to that point!")
        except:
            print("An exception occured!")
        return returnPA

    def intervention_solved(self):
        self.set_vehicle_status("AUTO_DRIVING")
        TraciHandler.driveToNextParkingAreaWasCalled = True
        self.setNewParkingPosLatLon(TraciServer.FILTER_POSITION_LAT, TraciServer.FILTER_POSITION_LON)

    def hard_fault_solved(self):
        self.set_vehicle_status("PARKING")


    def get_current_target_position(self):
        if self.get_vehicle_status() == "HARD_FAULT":
            return None
        if self.nextPaID == self.get_closest_parking_area(TraciServer.INTERVENTION_LAT, TraciServer.INTERVENTION_LON)["id"]:
            return self.get_closest_parking_area(TraciServer.FILTER_POSITION_LAT, TraciServer.FILTER_POSITION_LON)
        for pa in TraciHandler.parkingAreaList:
            if pa["id"] == self.nextPaID:
                return pa
        return None


################ --- UPDATE VEHICLE STATUS --- ######################
    
    def get_current_van_position(self):
        return (self.current_van_lat_geo, self.current_van_long_geo)


    def set_vehicle_status(self, status):
        for x in range(0, len(TraciServer.VEHICLE_STATES)):
            if TraciServer.VEHICLE_STATES[x] == status:
                self.vehicle_status = x

    
    def get_vehicle_status(self):
        return TraciServer.VEHICLE_STATES[self.vehicle_status]

    def get_vehicle_door_status(self):
        return self.door_status

    def set_vehicle_door_status(self, door_status):
        self.door_status = door_status
        if door_status == "DOORS_OPEN" and self.get_vehicle_status() == "PARKING":
            self.set_vehicle_status("DOORS_OPEN")
        elif self.get_vehicle_status() == "DOORS_OPEN" and door_status == "DOORS_CLOSED":
            self.set_vehicle_status("PARKING")

    def get_vehicle_problem_status(self):
        return self.problem_status

    def set_vehicle_problem_status(self, problem_status):
        self.problem_status = problem_status

    def get_vehicle_problem_message(self):
        return self.problem_message

    def set_vehicle_problem_message(self, problem_message):
        self.problem_message = problem_message

    def update_fcm_token(self, fcm_token):
        self.fcm_token = fcm_token


################ --- PARKING AREA UTILITIES --- ######################

    def get_closest_parking_area(self, lat, lon):
        x = (lat, lon)
        distances = {}
        for x in range(0, len(TraciHandler.parkingAreaList)):
            pa = TraciHandler.parkingAreaList[x]
            distance = self.get_euclidean_distance(lat, pa["lat"], lon, pa["long"])
            distances[x] = distance
        min_x = min(distances, key=distances.get)

        return TraciHandler.parkingAreaList[min_x]

    def get_euclidean_distance(self, x1, x2, y1, y2):
        x = (x1-x2)**2
        y = (y1-y2)**2
        return math.sqrt(x+y)

       #########################################################
    # SelectNextParking
    # Current Location of the van
    # return closest parkingLocation (for now the name, later the id)
    def selectNextParking(self, van_current_loc):
        from app.sumo import traci

        refCoordinate = van_current_loc
        full = {} # initialize dict
        paid = self.retrieve_parking_areas() #get list of all parkingAreas IDs
        for pa in paid:
            if TraciHandler.simulationIsRunning:
                capacity = traci.simulation.getParameter(pa, "parkingArea.capacity")
                occupancy = traci.simulation.getParameter(pa, "parkingArea.occupancy")
            diff = int(capacity) - int(occupancy)
            if diff == 0:  # full == True
                full[pa] = True
            else:
                full[pa] = False
        if self.checkFull(full):
            print("all Parking Areas are occupied. Check in 40 steps")
            #what to do, when no parking area available
            #not applicable for us, just assume they are all empty
            return  # if all parkingAreas - occupied, then stop

        print("\n Parking Areas currently not fully occupied are ...")
        coordinatesDict = {}
        for key, value in full.items():
            if not value:
                print(key)
                coordinatesDict[key] = self.retrieve_parking_areas_coordinates(key)

        print("\n The parking area which is the closest to get to is ...")
        distances = {}
        for key, value in coordinatesDict.items():
            (x1, y1) = refCoordinate
            (x2, y2) = value

            distance = traci.simulation.getDistance2D(float(x1), float(y1), float(x2), float(y2), False, True)
            distances[key] = distance

        s = [(k, distances[k]) for k in sorted(distances, key=distances.get, reverse=False)]

        # Print the first parking Area Name after sorting the parkingAreas by the distance between car and parkArea
        # This is the closest parkingArea
        for k, v in s:
            print(str(self.retrieve_parking_area_name(k)) + " with a distance of " + str(round(v, 2)) + " metres! \n")
            return self.retrieve_parking_area_name(k)
            break

        #########################################################
    # Parse XML with parkingAreas
    # Get the name of the parkingArea passed as parkingArea ID (paID)
    # return name of the searched ParkingArea
    def retrieve_parking_area_name(self, paID):
        path = self.configurePath("parkingAreas.add.xml")
        doc = etree.parse(path)
        paName = doc.xpath("//parkingArea[@id='" + paID + "']/@name")
        return paName[0]


################ --- ACTUAL SIMULATION HANDLING --- ######################

    """--------------IMPORTANT---------------"""
    """This Method starts and manages the simulation"""
    def start(self, seconds_since_midnight, fcm_token):
        self.configure()
        self.fcm_token = fcm_token
        import traci
        import traci.constants as tc
        import sumolib
        from sumolib import checkBinary
        self.configureGEOfromXY()
        sumoBinary = checkBinary('sumo') #('sumo-gui')
        self.sumoBinary = os.environ['SUMO_HOME'] + "/bin/sumo"
        self.sumoCmd = [sumoBinary, "-c", os.path.dirname(os.path.realpath(__file__)) + "/config/ourSumoConfig.sumocfg", "--no-step-log", "true","--no-warnings","true" ,"--step-length", "1.0"] #, "--default.action-step-length", "2.0"]

        print("Rewriting the Routes File for faster Loading")
        self.routesPath = self.configurePath("activitygen_vanassist.rou.xml")
        self.routesEtree = etree.parse(self.routesPath)

        if seconds_since_midnight > 24000:
            for ele in self.routesEtree.xpath("//vehicle[@depart < '" + str(seconds_since_midnight) + "']"):
                ele.getparent().remove(ele)  # here I grab the parent of the element to call the remove directly on it

        try:
            file_path = self.configurePath("activitygen_vanassist_26.rou.xml")
            exists = os.path.isfile(file_path)
            print(exists)
            if exists:
            # delete file
                os.remove(file_path)
                print("success")
        except:
            print("unhandled file exception")

        new_path = self.configurePath("activitygen_vanassist_26.rou.xml")
        self.routesEtree.write(new_path)

        exists = os.path.isfile(file_path)
        while(exists == False):
            """wait"""
            time.sleep(1)
            exists = os.path.isfile(file_path)
        print("Starting the TraCI server...")
        traci.start(self.sumoCmd)
        TraciHandler.step = 0
        self.step = 0
        isWhile = True
        idList = []
        self.step = seconds_since_midnight
        traci.simulation.step(float(seconds_since_midnight))
        print("********* LOOP")
        traci.vehicle.add(str('dpd_van'), routeID='', typeID='dpd', depart=None, departLane='first', departPos='base',
                          departSpeed='0', arrivalLane='current', arrivalPos='max', arrivalSpeed='current', fromTaz='',
                          toTaz='', line='', personCapacity=2, personNumber=1)

        traci.vehicle.setRouteID('dpd_van', 'routeDPD')

        """Checks if the simulation was stopped from the app or it run for longer than one day (86400 seconds)"""
        while TraciHandler.stopSimulation==False and self.step <= 86400:

            starttime = time.time()
            """Nesessary because simulation is laggin at beginnin, just prints smooth after 1 step"""
            if self.step == seconds_since_midnight + 2:
                TraciHandler.simulationIsRunning = True
                self.set_vehicle_status("PARKING")
                if self.fcm_token != "" and self.fcm_token != None:
                    FirebaseCloudMessaging.sendMessage(self.fcm_token, CloudMessage.SIMULATION_START)

            print(str(self.step))
            if (self.step > seconds_since_midnight + 2) and TraciHandler.driveToNextParkingAreaWasCalled:
                print("Is stopped parking?")
                print(traci.vehicle.isStoppedParking(vehID='dpd_van'))
                self.set_vehicle_status("AUTO_DRIVING")
                self.parkingArrived = traci.vehicle.isStoppedParking(vehID='dpd_van')

        #SEND LOCATION UPDATES
                """Updates the van location every 3 seconds"""
                if self.step % 3 == 0:
                    van_lat_sumo, van_long_sumo  = traci.vehicle.getPosition(vehID='dpd_van')
                    (van_long_geo, van_lat_geo) = self.convertGEOfromXYWithoutConfiguration(van_lat_sumo, van_long_sumo)
                    self.current_van_lat_geo = van_lat_geo
                    self.current_van_long_geo = van_long_geo
                    if self.fcm_token != "" and self.fcm_token != None:
                        FirebaseCloudMessaging.sendCurrentPosition(self.fcm_token, CloudMessage.CURRENT_VAN_LOCATION, van_lat_geo, van_long_geo)

        #SEND NOTIFICATION WHEN DESTINATION IS REACHED
                """Sends a notification to the app when the van has arrived in its paking position"""
                if(self.parkingArrived and self.rerouteStarted):
                    if self.fcm_token != "" and self.fcm_token != None:
                        FirebaseCloudMessaging.sendMessage(self.fcm_token, CloudMessage.VEHICLE_IS_IN_NEXT_PARKING_AREA)
                    
                    #WHEN VEHICLE ARRIVED AT SPECIFIED INTERVENTION AREA
                    if self.nextPaID == self.get_closest_parking_area(TraciServer.INTERVENTION_LAT, TraciServer.INTERVENTION_LON)["id"]:
                        #self.sim_service.send_vehicle_intervention(vehicle_simulation_config.VEHICLE_ID, TraciServer.INTERVENTION_LAT, TraciServer.INTERVENTION_LON)
                        self.set_vehicle_status("INTERVENTION")
                    else:
                        current_target = self.get_current_target_position()
                        self.sim_service.send_position_reached(vehicle_simulation_config.VEHICLE_ID, current_target["lat"], current_target["long"])
                        self.set_vehicle_status("PARKING")
                    
                    TraciHandler.driveToNextParkingAreaWasCalled = False
                    self.rerouteStarted = False

        #CHECK WHETHER THE VEHICLE IS REQUESTED TO DRIVE TO A NEW PARKING AREA
            if self.checkNewPark == True:
                print("Target edge: " + str(self.nextPaEdge))
                print("Target PArea: " + str(self.nextPaID))
                traci.vehicle.changeTarget(vehID='dpd_van', edgeID=self.nextPaEdge)
                traci.vehicle.setParkingAreaStop(vehID='dpd_van', stopID=self.nextPaID, until=86400.0, flags=65)
                if traci.vehicle.isStopped('dpd_van'):
                    traci.vehicle.resume('dpd_van')
                    print("Parking triggered")
                self.rerouteStarted = True
                self.checkNewPark = False

            time.sleep(1.0 - ((time.time() - starttime) % 1.0))
            self.step += 1
            traci.simulationStep(self.step)

        #STOP THE SERVER
        print("Stopping the TraCI server...")
        self.nextPaID = ""
        self.nextPaEdge = ""
        self.checkNewPark = False
        TraciHandler.driveToNextParkingAreaWasCalled = False
        traci.close()
        if self.fcm_token != "" and self.fcm_token != None:
            FirebaseCloudMessaging.sendMessage(self.fcm_token, CloudMessage.SIMULATION_STOP)
        print("TraCI server stopped")
        TraciHandler.simulationIsRunning = False
        TraciHandler.startSimulationWasCalledFirst = False
        TraciHandler.stopSimulation = False
        sys.stdout.flush()
        position = "Traci Instance needs to start first"

        self.sumoBinary = None
        self.sumoCmd = None
        gc.collect()


