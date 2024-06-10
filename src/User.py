import uuid
import hashlib
from DBconnection import databaseConnection
import time

class User:
    def __init__(self, userRole, name, email, password, phone):
        self.userRole = userRole
        self.name = name
        self.email = email
        self.hashedPassword = self.hashPassword(password)
        self.phone = phone

    @staticmethod
    def hashPassword(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def signUp():
        print("Crear usuario")
        userRole = input("Ingrese el rol del usuario::: 1 si quiere ser host y 0 si quiere ser usuario: ")
        name = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el email del usuario: ")
        password = input("Ingrese la contraseña del usuario: ")
        hashedPassword = User.hashPassword(password)
        phone = input("Ingrese el teléfono del usuario: ")
        print("Creando usuario...")
        time.sleep(2)

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)

            userId = str(uuid.uuid4())

            cur.execute("""
                INSERT INTO user (userId, userRole, name, email, hashedPassword, phone)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (userId, userRole, name, email, hashedPassword, phone))

            conn.commit()
            print("Usuario creado con éxito")

        except Exception as e:
            print(f"Error al crear el usuario: {e}")
        
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def logIn():
        attempts = 0
        while attempts < 3:
            email = input("Ingrese el email del usuario: ")
            password = input("Ingrese la contraseña del usuario: ")
            hashedPassword = User.hashPassword(password)

            try:
                db = databaseConnection()
                conn = db.getConnection()
                if not conn:
                    raise Exception("No se pudo establecer la conexión a la base de datos.")
                
                cur = db.getCursor(conn)
                cur.execute("SELECT * FROM user WHERE email = %s AND hashedPassword = %s", (email, hashedPassword))
                user = cur.fetchone()
                if user:
                    print(f"Bienvenido {user[2]}")
                    break
                else:
                    print("Email o contraseña incorrectos")
                    attempts += 1

            except Exception as e:
                print(f"Error al iniciar sesión: {e}")

            finally:
                if 'cur' in locals():
                    cur.close()
                if 'conn' in locals():
                    conn.close()

        else:
            print("Número de intentos excedido")

    @staticmethod
    def getUserRole(email):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT userRole FROM user WHERE email = %s", (email,))
            userRole = cur.fetchone()
            cur.close()
            conn.close()
            if userRole:
                return userRole[0]
            else:
                print("Usuario no encontrado")
                return None

        except Exception as e:
            print(f"Error al obtener el rol del usuario: {e}")
            return None

    @staticmethod
    def getUserId(email):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            
            cur = db.getCursor(conn)
            cur.execute("SELECT userId FROM user WHERE email = %s", (email,))
            userId = cur.fetchone()
            cur.close()
            conn.close()
            if userId:
                return userId[0]
            else:
                print("Usuario no encontrado")
                return None

        except Exception as e:
            print(f"Error al obtener el ID del usuario: {e}")
            return None

    @staticmethod
    def isAdmin(email):
        userRole = User.getUserRole(email)
        if userRole == "1":
            return True
        else:
            return False

    @staticmethod
    def whatsaap(phone):
        pass