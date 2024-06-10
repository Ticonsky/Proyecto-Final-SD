from DBconnection import databaseConnection
from Booking import Booking
from Property import Property
from User import User

class Bill:
    def __init__(self, bookingId, propertyId,propertyPrice, userId, billStatus):
        self.billId = None
        self.bookingId = bookingId
        self.propertyId = propertyId
        self.propertyPrice = propertyPrice
        self.userId = userId
        self.billStatus = billStatus

    @staticmethod
    def addBill():
        email = input("Ingrese el email del usuario: ")
        booking_id = input("Ingrese el ID de la reserva: ")
        property_name = input("Ingrese el nombre de la propiedad: ")
        bill_status = input("Ingrese el estado de la factura: ")
        user_id = User.getUserId(email)
        if not user_id:
            print("Usuario no encontrado.")
            return
        booking = Booking.getBookingById(booking_id)
        if not booking:
            print("Reserva no encontrada.")
            return
        property_id = Property.getPropertyId(property_name)
        if not property_id:
            print("Propiedad no encontrada.")
            return
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO bill (bookingId, propertyId, userId, billStatus)
                VALUES (%s, %s, %s, %s)
                """, (booking_id, property_id, user_id, bill_status))
            conn.commit()
            print("Factura agregada con éxito")
        except Exception as e:
            print(f"Error al agregar la factura: {e}")
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def getBillById(billId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("SELECT * FROM bill WHERE billId = %s", (billId,))
            bill = cur.fetchone()
        except Exception as e:
            print(f"Error al obtener la factura: {e}")
            bill = None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        if bill:
            return bill
        else:
            print("Factura no encontrada")
            return None