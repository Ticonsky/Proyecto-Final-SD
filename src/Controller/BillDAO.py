from Model.DBconnetion import databaseConnection
from Model.BillVO import bill
from Model.BookingVO import Booking
from Model.PropertyVO import property
from Model.UserVO import user
from Controller.BookingDAO import bookingDAO
from Controller.PropertyDAO import PropertyDAO
from Controller.UserDAO import UserDAO
import uuid

class billDAO:
    def __init__(self):
        self.bookingDAO = bookingDAO()
        self.propertyDAO = PropertyDAO()
        self.userDAO = UserDAO()
    
    def create_bill(self, booking: Booking, property: property, user: user, billStatus):
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return
        
        userId = userId_result[0]
        propertyId = self.propertyDAO.getPropertyId(property.location, property.name)
        if propertyId is None:
            print("Propiedad no encontrada")
            return
        
        bookingId = self.bookingDAO.get_booking_id(userId, propertyId)
        if bookingId is None:
            print("Reserva no encontrada")
            return
        
        billId = str(uuid.uuid4())
        
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO bill (billId, bookingId, propertyId, propertyPrice, userId, billStatus)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (billId, bookingId, propertyId, property.price, userId, billStatus))
            
            conn.commit()
        except Exception as e:
            print(f"Error al crear la factura: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    
    def get_all_bills(self):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT * FROM bill")
            bills = cur.fetchall()
            return bills
        except Exception as e:
            print(f"Error al obtener todas las facturas: {e}")
            return []
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_bill_by_user_and_booking(self, userId, bookingId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM bill WHERE userId = %s AND bookingId = %s
                """, (userId, bookingId))
            bill = cur.fetchone()
            return bill
        except Exception as e:
            print(f"Error al obtener la factura: {e}")
            return None
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
