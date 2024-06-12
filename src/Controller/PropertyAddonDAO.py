from Model.PropertyAddonVO import propertyAddon
from Model.DBconnetion import databaseConnection

class PropertyAddonDAO:
    propertyAddonVO = propertyAddon("","","","","","","","",)

    def __init__(self):
        pass
    
    def get_propertyAddons(self, propertyAddon):
        wifi = propertyAddon.wifi
        kitchen = propertyAddon.kitchen
        parking = propertyAddon.parking
        staffService = propertyAddon.staffService
        pool = propertyAddon.pool
        securityCameras = propertyAddon.securityCameras
        laundry = propertyAddon.laundry
        gym = propertyAddon.gym
        
        wifi = True if wifi.upper() == "S" else False
        kitchen = True if kitchen.upper() == "S" else False
        parking = True if parking.upper() == "S" else False
        staffService = True if staffService.upper() == "S" else False
        pool = True if pool.upper() == "S" else False
        securityCameras = True if securityCameras.upper() == "S" else False
        laundry = True if laundry.upper() == "S" else False
        gym = True if gym.upper() == "S" else False

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
                """, (wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym))
            
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                print("No se encontró ninguna propiedad con esas características.")
                return None
        except Exception as e:
            print(f"Error al seleccionar el ID del complemento de propiedad: {e}")
            return None
        finally:
            if 'cur' in locals() and cur:
                try:
                    if cur._have_unread_result():
                        cur.fetchall()  # Leer todos los resultados no leídos
                except:
                    pass
                cur.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()
    def select_propertyAddon(self, propertyAddonId):
        
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM propertyaddon WHERE propertyAddonId = %s
                """, (propertyAddonId,))

            propertyAddon = cur.fetchone()
            return propertyAddon
        except Exception as e:
            print(f"Error al seleccionar el tipo de propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_propertyAddons(self, propertyAddon):
        wifi=propertyAddon.wifi
        kitchen=propertyAddon.kitchen
        parking=propertyAddon.parking
        staffService=propertyAddon.staffService
        pool=propertyAddon.pool
        securityCameras=propertyAddon.securityCameras
        laundry=propertyAddon.laundry
        gym=propertyAddon.gym
        wifi = True if wifi.upper() == "S" else False
        kitchen = True if kitchen.upper() == "S" else False
        parking = True if parking.upper() == "S" else False
        staffService = True if staffService.upper() == "S" else False
        pool = True if pool.upper() == "S" else False
        securityCameras = True if securityCameras.upper() == "S" else False
        laundry = True if laundry.upper() == "S" else False
        gym = True if gym.upper() == "S" else False
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
                """, (wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym))
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