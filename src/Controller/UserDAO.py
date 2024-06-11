from Model.UserVO import user
from Model.DBconnetion import databaseConnection 
import uuid
import hashlib

class UserDAO:
    UserVO = user("","","","","")
    def __init__(self):
        pass

    def hashpassword(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, user:user):
        # Código para crear un nuevo usuario en la base de datos
        userRole=user.userRole
        name = user.name
        email = user.email
        password = user.hashedPassword
        password=UserDAO.hashpassword(password)
        phone = user.phone
        user_id = str(uuid.uuid4())
        

        print(userRole, user_id,name, email, password, phone)
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO user (userRole,userId, name, email, hashedPassword, phone)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (userRole,user_id, name, email, password, phone))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def delete_user(self, user):
        name=user.name
        # Código para eliminar un usuario de la base de datos
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                DELETE FROM user WHERE name = %s
                """, (name))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def upgradeUser(self, user):
        # Código para actualizar un usuario en la base de datos
        name=user.name
        userRole=1
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                UPDATE user SET userRole = %s
                WHERE name = %s
                """, (name))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_userID(self, user):
        name= user.name
        # Código para obtener un usuario de la base de datos
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT userId FROM user WHERE name = %s
                """, (name,))

            user = cur.fetchone()
            return user
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
