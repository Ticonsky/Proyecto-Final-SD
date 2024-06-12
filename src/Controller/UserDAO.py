# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.UserVO import user
from Model.DBconnetion import databaseConnection 
import uuid
import hashlib

# Clase que maneja las operaciones de acceso a datos para los usuarios
class UserDAO:
    UserVO = user("", "", "", "", "")

    def __init__(self):
        pass

    # Método para cifrar la contraseña
    def hashpassword(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Método para crear un usuario
    def create_user(self, user: user):
        userRole = user.userRole
        name = user.name
        email = user.email
        password = user.hashedPassword
        password = UserDAO.hashpassword(password)
        phone = user.phone
        user_id = str(uuid.uuid4())

        print(userRole, user_id, name, email, password, phone)
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la inserción del usuario en la base de datos
            cur.execute("""
                INSERT INTO user (userRole, userId, name, email, hashedPassword, phone)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (userRole, user_id, name, email, password, phone))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para eliminar un usuario
    def delete_user(self, user):
        name = user.name
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la eliminación del usuario en la base de datos
            cur.execute("""
                DELETE FROM user WHERE name = %s
                """, (name,))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para actualizar el rol de un usuario
    def upgradeUser(self, user):
        name = user.name
        userRole = 1  # Asignar un nuevo rol (ejemplo: 1 para administrador)
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la actualización del rol del usuario en la base de datos
            cur.execute("""
                UPDATE user SET userRole = %s WHERE name = %s
                """, (userRole, name))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para obtener el ID de un usuario basado en su email
    def get_userID(self, user):
        email = user.email
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener el ID del usuario
            cur.execute("""
                SELECT userId FROM user WHERE email = %s
                """, (email,))

            result = cur.fetchone()
            if result:
                return result[0]  # Devuelve solo el ID de usuario
            else:
                print("Usuario no encontrado.")
                return None
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
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

    # Método para iniciar sesión de un usuario
    def LogIn(self, user):
        email = user.email
        password = user.hashedPassword
        password = UserDAO.hashpassword(password)
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para iniciar sesión del usuario
            cur.execute("""
                SELECT * FROM user WHERE email = %s AND hashedPassword = %s
                """, (email, password))

            user = cur.fetchone()
            return user
        except Exception as e:
            print(f"Error al iniciar sesión del usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para obtener el rol de un usuario basado en su email y contraseña
    def getUserRol(self, user: user):
        email = user.email
        password = user.hashedPassword
        password = UserDAO.hashpassword(password)
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener el rol del usuario
            cur.execute("""
                SELECT userRole FROM user WHERE email = %s AND hashedPassword = %s
                """, (email, password))

            userRole = cur.fetchone()
            return userRole
        except Exception as e:
            print(f"Error al obtener el rol del usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
        
    # Método para verificar si un usuario existe basado en su ID
    def check_user_exists(self, userId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para verificar la existencia del usuario
            cur.execute("SELECT COUNT(*) FROM user WHERE userId = %s", (userId,))
            result = cur.fetchone()
            return result[0] > 0
        except Exception as e:
            print(f"Error al verificar la existencia del usuario: {e}")
            return False
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
