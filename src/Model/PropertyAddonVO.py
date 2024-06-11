
class propertyAddon:
    def __init__(self, wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym):
        self.wifi = wifi
        self.kitchen = kitchen
        self.parking = parking
        self.staffService = staffService
        self.pool = pool
        self.securityCameras = securityCameras
        self.laundry = laundry
        self.gym = gym

    # Setters
    def set_wifi(self, wifi):
        self.wifi = wifi

    def set_kitchen(self, kitchen):
        self.kitchen = kitchen

    def set_parking(self, parking):
        self.parking = parking

    def set_staffService(self, staffService):
        self.staffService = staffService

    def set_pool(self, pool):
        self.pool = pool

    def set_securityCameras(self, securityCameras):
        self.securityCameras = securityCameras

    def set_laundry(self, laundry):
        self.laundry = laundry

    def set_gym(self, gym):
        self.gym = gym

    # Getters
    def get_wifi(self):
        return self.wifi

    def get_kitchen(self):
        return self.kitchen

    def get_parking(self):
        return self.parking

    def get_staffService(self):
        return self.staffService

    def get_pool(self):
        return self.pool

    def get_securityCameras(self):
        return self.securityCameras

    def get_laundry(self):
        return self.laundry

    def get_gym(self):
        return self.gym