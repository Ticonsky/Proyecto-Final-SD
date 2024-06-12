# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.PropertyTypeVO import propertyType
from Model.DBconnetion import databaseConnection
import uuid

# Clase que maneja las operaciones de acceso a datos para los tipos de propiedades
class PropertyTypeDAO:
    def __init__(self):
        pass

    propertyType = propertyType("", "")

    # Método para crear un tipo de propiedad
    def create_propertyType(self, propertyType):
        name = propertyType.name
        description = propertyType.description
        propertyTypeId = str(uuid.uuid4())

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la inserción del tipo de propiedad en la base de datos
            cur.execute("""
                INSERT INTO propertyType (propertyTypeId, name, description)
                VALUES (%s, %s, %s)
                """, (propertyTypeId, name, description))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el tipo de propiedad: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para eliminar un tipo de propiedad
    def delete_propertyType(self, propertyType):
        name = propertyType.name
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la eliminación del tipo de propiedad en la base de datos
            cur.execute("""
                DELETE FROM propertyType WHERE name = %s
                """, (name,))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar el tipo de propiedad: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
    
    # Método para actualizar un tipo de propiedad
    def update_propertyType(self, propertyType):
        propertyTypeId = propertyType.propertyTypeId
        name = propertyType.name
        description = propertyType.description

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la actualización del tipo de propiedad en la base de datos
            cur.execute("""
                UPDATE propertyType SET name = %s, description = %s WHERE propertyTypeId = %s
                """, (name, description, propertyTypeId))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar el tipo de propiedad: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
    
    # Método para obtener el ID de un tipo de propiedad basado en su nombre
    def get_propertyType(self, propertyType):
        name = propertyType.name
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener el ID del tipo de propiedad
            cur.execute("""
                SELECT propertyTypeId FROM propertyType WHERE name = %s
                """, (name,))
            propertyTypeId_result = cur.fetchone()
            if propertyTypeId_result:
                return propertyTypeId_result[0]  # Devolver solo el valor del ID
            else:
                print("Tipo de propiedad no encontrado")
                return None
        except Exception as e:
            print(f"Error al obtener el tipo de propiedad: {e}")
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
