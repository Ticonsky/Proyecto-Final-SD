from DBconnection import databaseConnection  # Importa DatabaseConnection
from User import User
from Property_type import propertyType
from Property_Addons import propertyAddon
import uuid
import requests

class Property:
    def __init__(self, userId, propertyType, propertyAddon, location, guests, rooms, beds, bathrooms, photos, name, description, price):
        self.userId = userId
        self.propertyType = propertyType
        self.propertyAddon = propertyAddon
        self.location = location
        self.guests = guests
        self.rooms = rooms
        self.beds = beds
        self.bathrooms = bathrooms
        self.photos = photos
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def addProperty():
        print("Por favor, ingrese los siguientes datos para agregar una propiedad.")
        email = input("Ingrese el email del usuario: ")

        user_id = User.getUserId(email)
        if not user_id:
            print("Usuario no encontrado.")
            return

        property_type = input("Ingrese el tipo de propiedad: ")
        propertyTypeId = propertyType.getPropertyTypeId(property_type)
        if not propertyTypeId:
            print("Tipo de propiedad no encontrado.")
            return

        propertyAddonId = propertyAddon.selectPropertyAddonId()
        if not propertyAddonId:
            print("Complemento de propiedad no encontrado.")
            return

        location = input("Ingrese la ubicación de la propiedad: ")
        guests = int(input("Ingrese la cantidad de huéspedes: "))
        rooms = int(input("Ingrese la cantidad de habitaciones: "))
        beds = int(input("Ingrese la cantidad de camas: "))
        bathrooms = int(input("Ingrese la cantidad de baños: "))
        photos = input("Ingrese la URL de las fotos: ")
        name = input("Ingrese el nombre de la propiedad: ")
        description = input("Ingrese la descripción de la propiedad: ")
        price = float(input("Ingrese el precio de la propiedad: "))

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            property_id = str(uuid.uuid4())
            cur.execute("""
                INSERT INTO property (propertyId, userId, propertyTypeId, propertyAddonId, location, guestsCapacity, availableRooms, availableBeds, availableBaths, media, name, description, price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (property_id, user_id, propertyTypeId, propertyAddonId, location, guests, rooms, beds, bathrooms, photos, name, description, price))

            conn.commit()
            print("Propiedad creada con éxito")

        except Exception as e:
            print(f"Error al crear la propiedad: {e}")

        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def getPropertyId(name):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT propertyId FROM Property WHERE name = %s", (name,))
            propertyId = cur.fetchone()
        
        except Exception as e:
            print(f"Error al obtener el ID de la propiedad: {e}")
            propertyId = None
        
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        
        if propertyId:
            return propertyId[0]
        else:
            print("Propiedad no encontrada")
            return None

    @staticmethod
    def getPropertyPrice(name):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT price FROM Property WHERE name = %s", (name,))
            propertyPrice = cur.fetchone()
        
        except Exception as e:
            print(f"Error al obtener el precio de la propiedad: {e}")
            propertyPrice = None
        
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        
        if propertyPrice:
            return propertyPrice[0]
        else:
            print("Propiedad no encontrada")
            return None
        
    @staticmethod
    def getLocation():
        name = input("Ingrese el nombre de la propiedad: ")
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT location FROM Property WHERE name = %s", (name,))
            location = cur.fetchall()
        
        except Exception as e:
            print(f"Error al obtener la ubicación de la propiedad: {e}")
            location = None
        
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        
        if location:
            return location
        else:
            print("Propiedad no encontrada")
            return None

    def get_coordinates(location):
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response_data = response.json()
        
        if response_data:
            lat = response_data[0]['lat']
            lon = response_data[0]['lon']
            return lat, lon
        else:
            raise Exception("Error fetching coordinates")

    def generate_osm_url(lat, lon):
        return f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=16"

    def URLocation(location):
        
        try:
            lat, lon = property.get_coordinates(location)
            osm_url = property.generate_osm_url(lat, lon)
            print(f"La URL de OpenStreetMap es: {osm_url}")
        except Exception as e:
            print(f"Error: {e}")
#api para obtener la ubicacion de la propiedad y generar la url de openstreetmap para mostrar la ubicacion de la propiedad en un mapa en la pagina web de la aplicacion de alquiler de propiedades


