
from src.Model.BookingVO import booking
from src.Model.PropertyVO import property
from src.Model.UserVO import user

class bill:
    def __init__(self, bookingId, propertyId,propertyPrice, userId, billStatus):
        self.billId = None
        self.bookingId = bookingId
        self.propertyId = propertyId
        self.propertyPrice = propertyPrice
        self.userId = userId
        self.billStatus = billStatus
    def get_billId(self):
        return self.billId

    def set_billId(self, billId):
        self.billId = billId

    def get_bookingId(self):
        return self.bookingId

    def set_bookingId(self, bookingId):
        self.bookingId = bookingId

    def get_propertyId(self):
        return self.propertyId

    def set_propertyId(self, propertyId):
        self.propertyId = propertyId

    def get_propertyPrice(self):
        return self.propertyPrice

    def set_propertyPrice(self, propertyPrice):
        self.propertyPrice = propertyPrice

    def get_userId(self):
        return self.userId

    def set_userId(self, userId):
        self.userId = userId

    def get_billStatus(self):
        return self.billStatus

    def set_billStatus(self, billStatus):
        self.billStatus = billStatus