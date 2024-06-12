from Model.CardVO import card
from Model.DBconnetion import databaseConnection
import uuid
from Model.UserVO import user
from Controller.UserDAO import UserDAO

class CardDAO:
    CardVO = card("","","","","","")
    
    userDAO = UserDAO()
    uservo = user("","","","","")
    def __init__(self):
        pass

    def create_card(self, card, user: user):
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return
        userId = userId_result[0]  # Acceder al primer elemento de la tupla devuelta por fetchone()


    def __init__(self):
        pass

    def create_card(self, card):
        userVO = user()
        userdao=UserDAO()
        userId = userdao.get_userId(userVO) 

        cardNumber = card.cardNumber
        cardOwner = card.cardOwner
        dueDate = card.dueDate
        cvv = card.cvv
        balance = card.balance
        cardId = str(uuid.uuid4())
        print(cardOwner)


        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")
            cur = db.getCursor(conn)
            print(userId)
            cur.execute("""
                INSERT INTO card (cardId, userId, cardNumber, cardOwner, dueDate, cvv, balance)
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

    def get_cardID(self, cardNumber, user: user):
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return None

        userId = userId_result[0]  # Acceder al primer elemento de la tupla devuelta por fetchone()

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
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
            if conn.is_connected():
                cur.close()
                conn.close()

