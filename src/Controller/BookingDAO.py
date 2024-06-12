# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.UserVO import user
from Model.PropertyVO import property
from Controller.UserDAO import UserDAO
from Controller.PropertyDAO import PropertyDAO
from Model.DBconnetion import databaseConnection
from Model.BookingVO import Booking
import uuid

# Clase que maneja las operaciones de acceso a datos para las reservas
class bookingDAO:
    booking = Booking("", "", "", "")

    def __init__(self):
        # Constructor de la clase bookingDAO
        self.userDAO = UserDAO()  # DAO para manejar las operaciones de usuarios
        self.propertyDAO = PropertyDAO()  # DAO para manejar las operaciones de propiedades

    # Método para crear una reserva
    def create_booking(self, property: property, user: user, checkIn, checkOut):
        # Obtener el ID del usuario
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return

        userId = userId_result[0]
        # Obtener el ID de la propiedad
        propertyId = self.propertyDAO.getPropertyId(property)
        if propertyId is None:
            print("Propiedad no encontrada")
            return
        
        bookingId = str(uuid.uuid4())
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la inserción de la reserva en la base de datos
            cur.execute("""
                INSERT INTO booking (bookingId, userId, propertyId, startingDate, endingDate)
                VALUES (%s, %s, %s, %s, %s)
                """, (bookingId, userId, propertyId, checkIn, checkOut))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la reserva: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para eliminar una reserva
    def delete_booking(self, userId, propertyId):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            # Ejecutar la eliminación de la reserva en la base de datos
            cur.execute("""
                DELETE FROM booking WHERE userId = %s AND propertyId = %s
                """, (userId, propertyId))
            
            conn.commit()
        except Exception as e:
            print(f"Error al eliminar la reserva: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para actualizar las fechas de una reserva
    def update_booking_dates(self, userId, propertyId, newCheckIn, newCheckOut):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            # Ejecutar la actualización de las fechas de la reserva en la base de datos
            cur.execute("""
                UPDATE booking 
                SET startingDate = %s, endingDate = %s
                WHERE userId = %s AND propertyId = %s
                """, (newCheckIn, newCheckOut, userId, propertyId))
            
            conn.commit()
        except Exception as e:
            print(f"Error al actualizar las fechas de la reserva: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para obtener todas las reservas
    def get_all_bookings(self):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener todas las reservas
            cur.execute("""
                SELECT * FROM booking
                """)
            
            bookings = cur.fetchall()
            return bookings
        except Exception as e:
            print(f"Error al obtener todas las reservas: {e}")
            return []
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
    
    # Método para obtener el ID de una reserva específica
    def get_booking_id(self, userId, propertyId):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener el ID de la reserva
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
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                try:
                    if cur._have_unread_result():
                        cur.fetchall()  # Leer todos los resultados no leídos
                except:
                    pass
                cur.close()
                conn.close()
