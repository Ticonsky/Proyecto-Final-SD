class property:
    def __init__(self, userId, propertyType, propertyAddon, location, guests, rooms, beds, bathrooms, photos, name, description, price):
        self.userId = userId
        self.propertyType = propertyType
        self.propertyAddon = propertyAddon
        self.location = location
        self.guests = guests
        self.rooms = rooms
        self.beds = beds
        self.bathrooms = bathrooms
        self.photos = photos
        self.name = name
        self.description = description
        self.price = price

    def get_userId(self):
        return self.userId

    def set_userId(self, userId):
        self.userId = userId

    def get_propertyType(self):
        return self.propertyType

    def set_propertyType(self, propertyType):
        self.propertyType = propertyType

    def get_propertyAddon(self):
        return self.propertyAddon

    def set_propertyAddon(self, propertyAddon):
        self.propertyAddon = propertyAddon

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_guests(self):
        return self.guests

    def set_guests(self, guests):
        self.guests = guests

    def get_rooms(self):
        return self.rooms

    def set_rooms(self, rooms):
        self.rooms = rooms

    def get_beds(self):
        return self.beds

    def set_beds(self, beds):
        self.beds = beds

    def get_bathrooms(self):
        return self.bathrooms

    def set_bathrooms(self, bathrooms):
        self.bathrooms = bathrooms

    def get_photos(self):
        return self.photos

    def set_photos(self, photos):
        self.photos = photos

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price