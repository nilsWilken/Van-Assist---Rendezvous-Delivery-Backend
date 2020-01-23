class Location:
    latitude=0
    longitude=0

    def __init__(self, latitude, longitude): # pragma: no cover
        self.latitude = latitude
        self.longitude = longitude

    def serialize(self): # pragma: no cover
        return {
            'latitude':self.latitude,
            'longitude':self.longitude
        }