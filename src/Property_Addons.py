from DBconnection import databaseConnection  # Asegúrate de que el import sea correcto

class propertyAddon:
    def __init__(self, wifi, kitchen, parking, staffService, pool, securityCameras, laundry, gym):
        self.wifi = wifi
        self.kitchen = kitchen
        self.parking = parking
        self.staffService = staffService
        self.pool = pool
        self.securityCameras = securityCameras
        self.laundry = laundry
        self.gym = gym

    @staticmethod
    def selectPropertyAddonId():
        print("Por favor, responda las siguientes preguntas para seleccionar los complementos correspondientes.")
        wifi = input("¿Tiene wifi? (S/N): ")
        kitchen = input("¿Tiene cocina? (S/N): ")
        parking = input("¿Tiene estacionamiento? (S/N): ")
        staffService = input("¿Tiene servicio de personal? (S/N): ")
        pool = input("¿Tiene piscina? (S/N): ")
        securityCameras = input("¿Tiene cámaras de seguridad? (S/N): ")
        laundry = input("¿Tiene lavandería? (S/N): ")
        gym = input("¿Tiene gimnasio? (S/N): ")

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

    @staticmethod
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

