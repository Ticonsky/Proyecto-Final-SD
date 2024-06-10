from DBconnection import databaseConnection  # Importa DatabaseConnection
from User import User
from Property import Property
import uuid

class Booking:
    def __init__(self, propertyId, userId, startingDate):
        self.bookingId = str(uuid.uuid4())
        self.propertyId = propertyId
        self.userId = userId
        self.startingDate = startingDate

    @staticmethod
    def addBooking():
        email = input("Ingrese el email del usuario: ")
        property_name = input("Ingrese el nombre de la propiedad: ")
        starting_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")

        user_id = User.getUserId(email)
        if not user_id:
            print("Usuario no encontrado.")
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
            booking_id = str(uuid.uuid4())
            cur.execute("""
                INSERT INTO booking (bookingId, propertyId, userId, startingDate)
                VALUES (%s, %s, %s, %s)
                """, (booking_id, property_id, user_id, starting_date))

            conn.commit()
            print("Reserva creada con éxito")

        except Exception as e:
            print(f"Error al crear la reserva: {e}")

        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def getBookingById(bookingId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT * FROM booking WHERE bookingId = %s", (bookingId,))
            booking = cur.fetchone()
        
        except Exception as e:
            print(f"Error al obtener la reserva: {e}")
            booking = None
        
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        
        if booking:
            return booking
        else:
            print("Reserva no encontrada")
            return None