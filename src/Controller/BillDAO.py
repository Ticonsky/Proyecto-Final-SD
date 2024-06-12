# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.DBconnetion import databaseConnection
from Model.BillVO import bill
from Model.BookingVO import Booking
from Model.PropertyVO import property
from Model.UserVO import user
from Controller.BookingDAO import bookingDAO
from Controller.PropertyDAO import PropertyDAO
from Controller.UserDAO import UserDAO
import uuid

# Clase que maneja las operaciones de acceso a datos para las facturas
class billDAO:
    def __init__(self):
        # Constructor de la clase billDAO
        self.bookingDAO = bookingDAO()  # DAO para manejar las operaciones de reservas
        self.propertyDAO = PropertyDAO()  # DAO para manejar las operaciones de propiedades
        self.userDAO = UserDAO()  # DAO para manejar las operaciones de usuarios
    
    # Método para crear una factura
    def create_bill(self, booking: Booking, property: property, user: user, billStatus):
        # Obtener el ID del usuario
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return
        
        userId = userId_result[0]
        # Obtener el ID de la propiedad
        propertyId = self.propertyDAO.getPropertyId(property.location, property.name)
        if propertyId is None:
            print("Propiedad no encontrada")
            return
        
        # Obtener el ID de la reserva
        bookingId = self.bookingDAO.get_booking_id(userId, propertyId)
        if bookingId is None:
            print("Reserva no encontrada")
            return
                
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            # Ejecutar la inserción de la factura en la base de datos
            cur.execute("""
                INSERT INTO bill (bookingId, propertyId, propertyPrice, userId, billStatus)
                VALUES (%s, %s, %s, %s, %s)
                """, (bookingId, propertyId, property.price, userId, billStatus))
            
            conn.commit()
        except Exception as e:
            print(f"Error al crear la factura: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
    
    # Método para obtener todas las facturas
    def get_all_bills(self):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener todas las facturas
            cur.execute("SELECT * FROM bill")
            bills = cur.fetchall()
            return bills
        except Exception as e:
            print(f"Error al obtener todas las facturas: {e}")
            return []
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para obtener una factura por ID de usuario e ID de reserva
    def get_bill_by_user_and_booking(self, userId, bookingId):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            
            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener la factura específica
            cur.execute("""
                SELECT * FROM bill WHERE userId = %s AND bookingId = %s
                """, (userId, bookingId))
            bill = cur.fetchone()
            return bill
        except Exception as e:
            print(f"Error al obtener la factura: {e}")
            return None
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
