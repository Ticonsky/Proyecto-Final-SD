from Model.UserVO import user
from Model.PropertyVO import property
from Controller.UserDAO import UserDAO
from Controller.PropertyDAO import PropertyDAO
from Model.DBconnetion import databaseConnection
from Model.BookingVO import Booking
import uuid


class bookingDAO:
    booking = Booking("","","","")

    def __init__(self):
        self.userDAO = UserDAO()
        self.propertyDAO = PropertyDAO()

    def create_booking(self, property: property, user: user, checkIn, checkOut):
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return

        userId = userId_result[0]
        propertyId = self.propertyDAO.getPropertyId(property)
        if propertyId is None:
            print("Propiedad no encontrada")
            return
        
        bookingId = str(uuid.uuid4())
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO booking (bookingId, userId, propertyId, startingDate, endingDate)
                VALUES (%s, %s, %s, %s, %s)
                """, (bookingId, userId, propertyId, checkIn, checkOut))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la reserva: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def delete_booking(self, userId, propertyId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            cur.execute("""
                DELETE FROM booking WHERE userId = %s AND propertyId = %s
                """, (userId, propertyId))
            
            conn.commit()
        except Exception as e:
            print(f"Error al eliminar la reserva: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def update_booking_dates(self, userId, propertyId, newCheckIn, newCheckOut):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            cur.execute("""
                UPDATE booking 
                SET startingDate = %s, endingDate = %s
                WHERE userId = %s AND propertyId = %s
                """, (newCheckIn, newCheckOut, userId, propertyId))
            
            conn.commit()
        except Exception as e:
            print(f"Error al actualizar las fechas de la reserva: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_all_bookings(self):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM booking
                """)
            
            bookings = cur.fetchall()
            return bookings
        except Exception as e:
            print(f"Error al obtener todas las reservas: {e}")
            return []
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    
    def get_booking_id(self, userId, propertyId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT bookingId FROM booking WHERE userId = %s AND propertyId = %s
                """, (userId, propertyId))
            
            result = cur.fetchone()
            if result:
                return result[0]  # Devolver solo el valor del ID de la reserva
            else:
                print("Reserva no encontrada con el usuario y propiedad proporcionados.")
                return None
        except Exception as e:
            print(f"Error al obtener el ID de la reserva: {e}")
            return None
        finally:
            if conn.is_connected():
                try:
                    if cur._have_unread_result():
                        cur.fetchall()  # Leer todos los resultados no leídos
                except:
                    pass
                cur.close()
                conn.close()
