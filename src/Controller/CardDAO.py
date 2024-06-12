# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.CardVO import card
from Model.DBconnetion import databaseConnection
import uuid
from Model.UserVO import user
from Controller.UserDAO import UserDAO

# Clase que maneja las operaciones de acceso a datos para las tarjetas
class CardDAO:
    CardVO = card("", "", "", "", "", "")
    userDAO = UserDAO()
    uservo = user("", "", "", "", "")
    
    def __init__(self):
        pass

    # Método para crear una tarjeta
    def create_card(self, card, user: user):
        # Obtener el ID del usuario
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return
        userId = userId_result[0]  # Acceder al primer elemento de la tupla devuelta por fetchone()

        cardNumber = card.cardNumber
        cardOwner = card.cardOwner
        dueDate = card.dueDate
        cvv = card.cvv
        balance = card.balance
        cardId = str(uuid.uuid4())

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la inserción de la tarjeta en la base de datos
            cur.execute("""
                INSERT INTO card (cardId, userId, cardNumber, cardOwner, dueDate, cvv, balance)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (cardId, userId, cardNumber, cardOwner, dueDate, cvv, balance))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la tarjeta: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para eliminar una tarjeta
    def delete_card(self, cardId):
        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la eliminación de la tarjeta en la base de datos
            cur.execute("""
                DELETE FROM cards WHERE cardId = %s
                """, (cardId,))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar la tarjeta: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para actualizar una tarjeta
    def update_card(self, card):
        cardId = card.cardId
        userId = card.userId
        cardNumber = card.cardNumber
        cardOwner = card.cardOwner
        dueDate = card.dueDate
        cvv = card.cvv
        balance = card.balance

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la actualización de la tarjeta en la base de datos
            cur.execute("""
                UPDATE cards SET userId = %s, cardNumber = %s, cardOwner = %s, dueDate = %s, cvv = %s, balance = %s
                WHERE cardId = %s
                """, (userId, cardNumber, cardOwner, dueDate, cvv, balance, cardId))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar la tarjeta: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()

    # Método para obtener el ID de una tarjeta específica
    def get_cardID(self, cardNumber, user: user):
        # Obtener el ID del usuario
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return None

        userId = userId_result[0]  # Acceder al primer elemento de la tupla devuelta por fetchone()

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la consulta para obtener el ID de la tarjeta
            cur.execute("""
                SELECT cardId FROM card WHERE cardNumber = %s AND userId = %s
                """, (cardNumber, userId))
            
            cardId_result = cur.fetchone()
            if cardId_result:
                return cardId_result[0]
            else:
                print("Tarjeta no encontrada")
                return None
        except Exception as e:
            print(f"Error al obtener la tarjeta: {e}")
            return None
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
