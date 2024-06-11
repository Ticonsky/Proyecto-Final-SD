from Model.UserVO import user
from Model.DBconnetion import databaseConnection 
import uuid


class UserDAO:
    UserVO = user()
    def __init__(self):
        pass

    def create_user(self, user):
        # Código para crear un nuevo usuario en la base de datos
        name = user.username
        email = user.email
        password = user.password
        user_id = str(uuid.uuid4())

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO users (user_id, username, email, password)
                VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, password))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def delete_user(self, user_id):
        # Código para eliminar un usuario de la base de datos
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                DELETE FROM users WHERE user_id = %s
                """, (user_id,))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def update_user(self, user):
        # Código para actualizar un usuario en la base de datos
        user_id = user.user_id
        name = user.username
        email = user.email
        password = user.password

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                UPDATE users SET username = %s, email = %s, password = %s
                WHERE user_id = %s
                """, (name, email, password, user_id))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_user(self, user_id):
        # Código para obtener un usuario de la base de datos
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM users WHERE user_id = %s
                """, (user_id,))

            user = cur.fetchone()
            return user
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
    