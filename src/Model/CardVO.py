
import uuid

class card:
    def __init__(self, userId, cardNumber, cardOwner, dueDate, cvv, balance, cardId=None):
        self.userId = userId
        self.cardNumber = cardNumber
        self.cardOwner = cardOwner
        self.dueDate = dueDate
        self.cvv = cvv
        self.balance = balance
        self.cardId = cardId or str(uuid.uuid4())

    def get_userId(self):
        return self.userId

    def set_userId(self, userId):
        self.userId = userId

    def get_cardNumber(self):
        return self.cardNumber

    def set_cardNumber(self, cardNumber):
        self.cardNumber = cardNumber

    def get_cardOwner(self):
        return self.cardOwner

    def set_cardOwner(self, cardOwner):
        self.cardOwner = cardOwner

    def get_dueDate(self):
        return self.dueDate

    def set_dueDate(self, dueDate):
        self.dueDate = dueDate

    def get_cvv(self):
        return self.cvv

    def set_cvv(self, cvv):
        self.cvv = cvv

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_cardId(self):
        return self.cardId

    def set_cardId(self, cardId):
        self.cardId = cardId
