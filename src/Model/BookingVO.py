

import uuid

class Booking:
    def __init__(self, propertyId, userId, startingDate, endingDate):
        self.bookingId = str(uuid.uuid4())
        self.propertyId = propertyId
        self.userId = userId
        self.startingDate = startingDate
        self.endingDate = endingDate

    # Setter for bookingId
    def setBookingId(self, bookingId):
        self.bookingId = bookingId

    # Getter for bookingId
    def getBookingId(self):
        return self.bookingId

    # Setter for propertyId
    def setPropertyId(self, propertyId):
        self.propertyId = propertyId

    # Getter for propertyId
    def getPropertyId(self):
        return self.propertyId

    # Setter for userId
    def setUserId(self, userId):
        self.userId = userId

    # Getter for userId
    def getUserId(self):
        return self.userId

    # Setter for startingDate
    def setStartingDate(self, startingDate):
        self.startingDate = startingDate

    # Getter for startingDate
    def getStartingDate(self):
        return self.startingDate