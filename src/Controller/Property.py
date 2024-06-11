from Model.PropertyAddonVO import propertyAddon
from Model.PropertyVO import property
from Model.DBconnetion import databaseConnection
from Model.PropertyTypeVO import propertyType
from Model.UserVO import user
import uuid

class Property:
    propertyAddonVO = propertyAddon()
    propertyVO = property()
    propertyTypeVO = propertyType()
    userVO = user()

    def __init__(self):
        pass

    def create_property(self, property):


        name = property.name
        description = property.description
        price = property.price
        propertyTypeId = property.propertyTypeId
        propertyId = str(uuid.uuid4())


        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO properties (propertyId, name, description, price, propertyTypeId)
                VALUES (%s, %s, %s, %s, %s)
                """, (propertyId, name, description, price, propertyTypeId))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def addAddonsProperty(self, property,propertyAddonsVO):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO propertyAddons (propertyId, wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (property.propertyId, propertyAddonsVO.wifi, propertyAddonsVO.kitchen, propertyAddonsVO.parking, propertyAddonsVO.staffService, propertyAddonsVO.pool, propertyAddonsVO.securityCameras, propertyAddonsVO.laundry, propertyAddonsVO.gym))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()