# Clase que representa un usuario
class user:
    
    def __init__(self, userRole, name, email, password, phone):
        # Constructor de la clase user, inicializa los atributos del usuario
        self.userRole = userRole  # Rol del usuario (e.g., administrador, cliente)
        self.name = name  # Nombre del usuario
        self.email = email  # Correo electrónico del usuario
        self.hashedPassword = password  # Contraseña del usuario (debe ser cifrada)
        self.phone = phone  # Número de teléfono del usuario

    # Métodos getter y setter para cada atributo de la clase user

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
        # Implementa tu lógica de cifrado de contraseñas aquí
        pass
