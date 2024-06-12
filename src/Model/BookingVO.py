# Importación del módulo uuid para generar identificadores únicos
import uuid

# Clase que representa una reserva
class Booking:
    def __init__(self, propertyId, userId, startingDate, endingDate):
        # Constructor de la clase Booking, inicializa los atributos de la reserva
        self.bookingId = str(uuid.uuid4())  # Genera un identificador único para la reserva
        self.propertyId = propertyId  # Identificador de la propiedad asociada a la reserva
        self.userId = userId  # Identificador del usuario que realiza la reserva
        self.startingDate = startingDate  # Fecha de inicio de la reserva
        self.endingDate = endingDate  # Fecha de finalización de la reserva

    # Métodos setter y getter para cada atributo de la clase Booking

    # Setter para bookingId
    def setBookingId(self, bookingId):
        self.bookingId = bookingId

    # Getter para bookingId
    def getBookingId(self):
        return self.bookingId

    # Setter para propertyId
    def setPropertyId(self, propertyId):
        self.propertyId = propertyId

    # Getter para propertyId
    def getPropertyId(self):
        return self.propertyId

    # Setter para userId
    def setUserId(self, userId):
        self.userId = userId

    # Getter para userId
    def getUserId(self):
        return self.userId

    # Setter para startingDate
    def setStartingDate(self, startingDate):
        self.startingDate = startingDate

    # Getter para startingDate
    def getStartingDate(self):
        return self.startingDate

    # Setter para endingDate
    def setEndingDate(self, endingDate):
        self.endingDate = endingDate

    # Getter para endingDate
    def getEndingDate(self):
        return self.endingDate
