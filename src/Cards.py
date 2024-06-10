from DBconnection import databaseConnection
import uuid
from User import User

class Card:
    def __init__(self, userId, cardNumber, cardOwner, dueDate, cvv, balance, cardId=None):
        self.userId = userId
        self.cardNumber = cardNumber
        self.cardOwner = cardOwner
        self.dueDate = dueDate
        self.cvv = cvv
        self.balance = balance
        self.cardId = cardId or str(uuid.uuid4())

    @staticmethod
    def addCard():
        email = input("Ingrese el email del usuario: ")
        userId = User.getUserId(email)
        if userId:
            cardNumber = input("Ingrese el número de la tarjeta: ")
            cardOwner = input("Ingrese el nombre del dueño de la tarjeta: ")
            dueDate = input("Ingrese la fecha de vencimiento de la tarjeta (MM/AA): ")
            cvv = input("Ingrese el CVV de la tarjeta: ")
            balance = float(input("Ingrese el saldo de la tarjeta: "))
            card = Card(userId, cardNumber, cardOwner, dueDate, cvv, balance)
            try:
                conn = databaseConnection().getConnection()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO card (cardId, userId, cardNumber, cardOwner, dueDate, cvv, balance)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (card.cardId, card.userId, card.cardNumber, card.cardOwner, card.dueDate, card.cvv, card.balance))
                conn.commit()
                print("Tarjeta creada con éxito")
            except Exception as e:
                print(f"Error al crear la tarjeta: {e}")
            finally:
                cur.close()
                conn.close()
        else:
            print("Usuario no encontrado")