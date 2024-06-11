from Model.PropertyTypeVO import propertyType
from Model.DBconnetion import databaseConnection

import uuid

class PropertyTypeDAO:
    def __init__(self):
        pass
    propertyType = propertyType("","")

    def create_propertyType(self, propertyType):
        name = propertyType.name
        description = propertyType.description
        propertyTypeId = str(uuid.uuid4())

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO propertyType (propertyTypeId, name, description)
                VALUES (%s, %s, %s)
                """, (propertyTypeId, name, description))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el tipo de propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def delete_propertyType(self, propertyType):
        name=propertyType.name
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                DELETE FROM propertyType WHERE name = %s
                """, (name,))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar el tipo de propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    
    def update_propertyType(self, propertyType):
        propertyTypeId = propertyType.propertyTypeId
        name = propertyType.name
        description = propertyType.description

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                UPDATE propertyType SET name = %s, description = %s WHERE propertyTypeId = %s
                """, (name, description, propertyTypeId))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar el tipo de propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    
    def get_propertyType(self, propertyTypeId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT  FROM propertyTypes WHERE propertyTypeId = %s
                """, (propertyTypeId,))

            propertyType = cur.fetchone()
            return propertyType
        except Exception as e:
            print(f"Error al obtener el tipo de propiedad: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    