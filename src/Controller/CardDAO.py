from Model.CardVO import card
from Model.DBconnetion import databaseConnection
import uuid
from Model.UserVO import user

class CardDAO:
    CardVO = card()
    def __init__(self):
        pass

    def create_card(self, card):
        # Código para crear una nueva tarjeta en la base de datos
        userId = card.userId
        cardNumber = card.cardNumber
        cardOwner = card.cardOwner
        dueDate = card.dueDate
        cvv = card.cvv
        balance = card.balance
        cardId = str(uuid.uuid4())

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO cards (cardId, userId, cardNumber, cardOwner, dueDate, cvv, balance)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (cardId, userId, cardNumber, cardOwner, dueDate, cvv, balance))

            conn.commit()
        except Exception as e:
            print(f"Error al crear la tarjeta: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def delete_card(self, cardId):
        # Código para eliminar una tarjeta de la base de datos
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                DELETE FROM cards WHERE cardId = %s
                """, (cardId,))

            conn.commit()
        except Exception as e:
            print(f"Error al eliminar la tarjeta: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def update_card(self, card):
        # Código para actualizar una tarjeta en la base de datos
        cardId = card.cardId
        userId = card.userId
        cardNumber = card.cardNumber
        cardOwner = card.cardOwner
        dueDate = card.dueDate
        cvv = card.cvv
        balance = card.balance

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                UPDATE cards SET userId = %s, cardNumber = %s, cardOwner = %s, dueDate = %s, cvv = %s, balance = %s
                WHERE cardId = %s
                """, (userId, cardNumber, cardOwner, dueDate, cvv, balance, cardId))

            conn.commit()
        except Exception as e:
            print(f"Error al actualizar la tarjeta: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

    def get_card(self, cardId):
        # Código para obtener una tarjeta de la base de datos
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                SELECT * FROM cards WHERE cardId = %s
                """, (cardId,))

            card = cur.fetchone()
            return card
        except Exception as e:
            print(f"Error al obtener la tarjeta: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()

