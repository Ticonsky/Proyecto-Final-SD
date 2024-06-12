from Model.PropertyAddonVO import propertyAddon
from Model.PropertyVO import property
from Model.DBconnetion import databaseConnection
from Model.PropertyTypeVO import propertyType
from Model.UserVO import user
from Controller.UserDAO import UserDAO
from Controller.PropertyTypeDAO import PropertyTypeDAO
from Controller.PropertyAddonDAO import PropertyAddonDAO
import uuid

class PropertyDAO:

    def __init__(self):
        self.userDAO = UserDAO()
        self.propertyTypeDAO = PropertyTypeDAO()
        self.propertyAddonDAO = PropertyAddonDAO()

    def create_property(self, property, user: user, propertyType:propertyType, propertyAddon: propertyAddon):
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

        propertyTypeId = self.propertyTypeDAO.get_propertyType(propertyType)
        if propertyTypeId is None:
            print("Tipo de propiedad no encontrado")
            return

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
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO property (propertyId, userId, propertyTypeId, propertyAddonId, location, guestsCapacity, availableRooms, availableBeds, availableBaths, media, name, description, price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (propertyId, userId, propertyTypeId, propertyAddonId, location, guests, rooms, beds, bathrooms, photos, name, description, price))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def getPropertyId(self, property: property):
            location = property.location
            name = property.name
            try:
                db = databaseConnection()
                conn = db.getConnection()
                if not conn:
                    raise Exception("No se pudo establecer la conexión a la base de datos")

                cur = db.getCursor(conn)
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
                if conn.is_connected():
                    try:
                        if cur._have_unread_result():
                            cur.fetchall()  # Leer todos los resultados no leídos
                    except:
                        pass
                    cur.close()
                    conn.close()
    def getAllProperties(self):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM property
                """)

            properties = cur.fetchall()
            return properties
        except Exception as e:
            print(f"Error al seleccionar todas las propiedades: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    