from DBconnection import databaseConnection

class propertyType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def addPropertyType():
        print("Por favor, ingrese los siguientes datos para agregar un tipo de propiedad.")
        name = input("Ingrese el nombre del tipo de propiedad: ")
        description = input("Ingrese la descripción del tipo de propiedad: ")
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO propertyType (name, description)
                VALUES (%s, %s)
                """, (name, description))
            conn.commit()
            print("Tipo de propiedad agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el tipo de propiedad: {e}")
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def getPropertyTypeId(name):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("SELECT propertyTypeId FROM propertyType WHERE name = %s", (name,))
            propertyTypeId = cur.fetchone()
        except Exception as e:
            print(f"Error al obtener el ID del tipo de propiedad: {e}")
            propertyTypeId = None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        if propertyTypeId:
            return propertyTypeId[0]
        else:
            print("Tipo de propiedad no encontrado")
            return None

    @staticmethod
    def selectPropertyType():
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("SELECT * FROM propertyType")
            propertyTypes = cur.fetchall()
        except Exception as e:
            print(f"Error al seleccionar los tipos de propiedad: {e}")
            propertyTypes = None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        return propertyTypes

    def getPropertyName(self):
        return self.name

    def getPropertyDescription(self):
        return self.description