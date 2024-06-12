# Importación de las clases necesarias para la factura
from Model.PropertyVO import property
from Model.UserVO import user
from Model.BookingVO import Booking

# Clase que representa una factura
class bill:
    def __init__(self, bookingId, propertyId, propertyPrice, userId, billStatus):
        # Constructor de la clase bill, inicializa los atributos de la factura
        self.billId = None  # Identificador único de la factura, inicialmente None
        self.bookingId = bookingId  # Identificador de la reserva asociada a la factura
        self.propertyId = propertyId  # Identificador de la propiedad asociada a la factura
        self.propertyPrice = propertyPrice  # Precio de la propiedad asociado a la factura
        self.userId = userId  # Identificador del usuario asociado a la factura
        self.billStatus = billStatus  # Estado de la factura (e.g., pagado, pendiente)
    
    # Métodos getter y setter para cada atributo de la clase bill
    
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
