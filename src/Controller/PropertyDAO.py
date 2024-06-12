# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.PropertyAddonVO import propertyAddon
from Model.PropertyVO import property
from Model.DBconnetion import databaseConnection
from Model.PropertyTypeVO import propertyType
from Model.UserVO import user
from Controller.UserDAO import UserDAO
from Controller.PropertyTypeDAO import PropertyTypeDAO
from Controller.PropertyAddonDAO import PropertyAddonDAO
import uuid

# Clase que maneja las operaciones de acceso a datos para las propiedades
class PropertyDAO:

    def __init__(self):
        # Constructor de la clase PropertyDAO
        self.userDAO = UserDAO()  # DAO para manejar las operaciones de usuarios
        self.propertyTypeDAO = PropertyTypeDAO()  # DAO para manejar las operaciones de tipos de propiedades
        self.propertyAddonDAO = PropertyAddonDAO()  # DAO para manejar las operaciones de complementos de propiedades

    # Método para crear una propiedad
    def create_property(self, property, user: user, propertyType: propertyType, propertyAddon: propertyAddon):
        # Obtener el ID del usuario
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return
        userId = userId_result[0]  # Acceder al primer elemento de la tupla devuelta por fetchone()

        # Verificar si el userId existe en la tabla de usuarios
        user_exists = self.userDAO.check_user_exists(userId)
        if not user_exists:
            print(f"Error: El userId {userId} no existe en la tabla de usuarios.")
            return

        # Obtener el ID del tipo de propiedad
        propertyTypeId = self.propertyTypeDAO.get_propertyType(propertyType)
        if propertyTypeId is None:
            print("Tipo de propiedad no encontrado")
            return

        # Obtener el ID del complemento de propiedad
        propertyAddonId = self.propertyAddonDAO.get_propertyAddons(propertyAddon)
        if propertyAddonId is None:
            print("Addon de propiedad no encontrado")
            return

        propertyId = str(uuid.uuid4())
        location = property.location
        guests = property.guests
        rooms = property.rooms
        beds = property.beds
        bathrooms = property.bathrooms
        photos = property.photos
        name = property.name
        description = property.description
        price = property.price

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la inserción de la propiedad en la base de datos
            cur.execute("""
                INSERT INTO property (propertyId, userId, propertyTypeId, propertyAddonId, location, guestsCapacity, availableRooms, availableBeds, availableBaths, media, name, description, price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (propertyId, userId, propertyTypeId, propertyAddonId, location, guests, rooms, beds, bathrooms, photos, name, description, price))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la propiedad: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para obtener el ID de una propiedad basada en su ubicación y nombre
    def getPropertyId(self, property: property):
        location = property.location
        name = property.name
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener el ID de la propiedad
            cur.execute("""
                SELECT propertyId FROM property WHERE location = %s AND name = %s
                """, (location, name))
            
            result = cur.fetchone()
            if result:
                return result[0]  # Devolver solo el valor del ID
            else:
                print("Propiedad no encontrada con la ubicación y nombre proporcionados.")
                return None
        except Exception as e:
            print(f"Error al obtener el ID de la propiedad: {e}")
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

    # Método para obtener todas las propiedades
    def getAllProperties(self):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener todas las propiedades
            cur.execute("""
                SELECT * FROM property
                """)

            properties = cur.fetchall()
            return properties
        except Exception as e:
            print(f"Error al seleccionar todas las propiedades: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
