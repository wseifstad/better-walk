class Address(object):
    """
    create address object initialized with
    address, latitude, longitude and trash_days
    """

    def __init__(self,address,lat,lng,trash_days):
        self.address = address
        self.lat = lat
        self.lng = lng
        self.trash_days = trash_days
    
    def get_address(cls):
        return cls.address

    def get_lat(cls):
        return cls.lat
    
    def get_lng(cls):
        return cls.lng
        
    def get_trash_days(cls):
        return cls.trash_days
