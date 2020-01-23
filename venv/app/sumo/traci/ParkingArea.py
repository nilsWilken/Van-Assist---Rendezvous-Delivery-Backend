class ParkingArea(object):
    id = ""
    name = ""
    length = 0
    lane = ""
    edge = ""
    roadsideCapacity = 0
    startPos = 0
    endPos = 0
    lat = 0
    long = 0
    x = 0
    y = 0


    def __init__(self, id, name, length, lane, edge, roadsideCap, startPos, endPos, lat, long, x, y):
        self.id = id
        self.name = name
        self.length = length
        self.lane = lane
        self.edge = edge
        self.roadsideCapacity = roadsideCap
        self.startPos = startPos
        self.endPos = endPos
        self.lat = lat
        self.long = long
        self.x = x
        self.y = y

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'length':self.length,
            'lane':self.lane,
            'edge':self.edge,
            'roadsideCapacity':self.roadsideCapacity,
            'startPos':self.startPos,
            'endPos':self.endPos,
            'lat': self.lat,
            'long': self.long,
            'x': self.x,
            'y': self.y
        }