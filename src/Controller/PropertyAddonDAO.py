from Model.PropertyAddonVO import propertyAddon
from Model.DBconnetion import databaseConnection
import uuid

class PropertyAddonDAO:
    def __init__(self):
        pass
    propertyAddonVO = propertyAddon()

    def select_propertyAddon(self, propertyAddonId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM propertyAddons WHERE propertyAddonId = %s
                """, (propertyAddonId,))

            propertyAddon = cur.fetchone()
            return propertyAddon
        except Exception as e:
            print(f"Error al seleccionar el tipo de propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_propertyAddons(self):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("""
                SELECT propertyAddonId 
                FROM propertyaddon
                WHERE wifi = %s AND kitchen = %s AND parking = %s AND staffService = %s AND pool = %s AND securityCameras = %s AND laundry = %s AND gym = %s
                """, (propertyAddon.wifi, propertyAddon.kitchen, propertyAddon.parking, propertyAddon.staffService, propertyAddon.pool, propertyAddon.securityCameras, propertyAddon.laundry, propertyAddon.gym))
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                print("No se encontró ninguna propiedad con esas características.")
        except Exception as e:
            print(f"Error al seleccionar el ID del complemento de propiedad: {e}")
            return None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()


    def setAllCombinations():
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cursor = db.getCursor(conn)
            combinations = []
            for b1 in [0, 1]:
                for b2 in [0, 1]:
                    for b3 in [0, 1]:
                        for b4 in [0, 1]:
                            for b5 in [0, 1]:
                                for b6 in [0, 1]:
                                    for b7 in [0, 1]:
                                        for b8 in [0, 1]:
                                            combinations.append((b1, b2, b3, b4, b5, b6, b7, b8))
            cursor.executemany(
                "INSERT INTO propertyaddon (wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                combinations
            )
            conn.commit()
            print("Combinaciones de Addons de propiedad agregadas con éxito")
        except Exception as e:
            print(f"Error al insertar combinaciones de complementos de propiedad: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close() 