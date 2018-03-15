class address_obj(object):
    """
    create address object initialized with
    address, latitude, longitude and trash_days
    """

    def __init__(self,address,lat,lng,trash_days):
        self.address = address
        self.lat = lat
        self.lng = lng
        self.trash_days = trash_days
    
    def get_address(self):
        return self.address

    def get_lat(self):
        return self.lat
    
    def get_lng(self):
        return self.lng
        
    def get_trash_days(self):
        return self.trash_days
