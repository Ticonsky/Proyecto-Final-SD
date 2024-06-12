
class user:
    
    def __init__():
        pass

    def __init__(self, userRole, name, email, password, phone):
        self.userRole = userRole
        self.name = name
        self.email = email
        self.hashedPassword = password
        self.phone = phone

    def getUserRole(self):
        return self.userRole

    def setUserRole(self, userRole):
        self.userRole = userRole

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def hashPassword(self, password):
        # Implement your password hashing logic here
        pass