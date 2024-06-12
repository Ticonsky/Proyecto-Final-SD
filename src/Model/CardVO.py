# Importación del módulo uuid para generar identificadores únicos
import uuid

# Clase que representa una tarjeta de crédito o débito
class card:
    def __init__(self, userId, cardNumber, cardOwner, dueDate, cvv, balance, cardId=None):
        # Constructor de la clase card, inicializa los atributos de la tarjeta
        self.userId = userId  # Identificador del usuario asociado a la tarjeta
        self.cardNumber = cardNumber  # Número de la tarjeta
        self.cardOwner = cardOwner  # Propietario de la tarjeta
        self.dueDate = dueDate  # Fecha de vencimiento de la tarjeta
        self.cvv = cvv  # Código de seguridad de la tarjeta
        self.balance = balance  # Saldo disponible en la tarjeta
        self.cardId = cardId or str(uuid.uuid4())  # Identificador único de la tarjeta, generado automáticamente si no se proporciona uno

    # Métodos getter y setter para cada atributo de la clase card

    # Getter para userId
    def get_userId(self):
        return self.userId

    # Setter para userId
    def set_userId(self, userId):
        self.userId = userId

    # Getter para cardNumber
    def get_cardNumber(self):
        return self.cardNumber

    # Setter para cardNumber
    def set_cardNumber(self, cardNumber):
        self.cardNumber = cardNumber

    # Getter para cardOwner
    def get_cardOwner(self):
        return self.cardOwner

    # Setter para cardOwner
    def set_cardOwner(self, cardOwner):
        self.cardOwner = cardOwner

    # Getter para dueDate
    def get_dueDate(self):
        return self.dueDate

    # Setter para dueDate
    def set_dueDate(self, dueDate):
        self.dueDate = dueDate

    # Getter para cvv
    def get_cvv(self):
        return self.cvv

    # Setter para cvv
    def set_cvv(self, cvv):
        self.cvv = cvv

    # Getter para balance
    def get_balance(self):
        return self.balance

    # Setter para balance
    def set_balance(self, balance):
        self.balance = balance

    # Getter para cardId
    def get_cardId(self):
        return self.cardId

    # Setter para cardId
    def set_cardId(self, cardId):
        self.cardId = cardId
