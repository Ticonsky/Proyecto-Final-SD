import sys
import os

# Añadir el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar los módulos necesarios

from Model.DBconnetion import databaseConnection
from Model.PropertyAddonVO import propertyAddon
from Model.PropertyTypeVO import propertyType
from Model.UserVO import user
from Model.PropertyVO import property
from Model.BookingVO import Booking
from Model.BillVO import bill
from Model.CommentVO import Comment
from Model.CardVO import card

from Controller.CardDAO import CardDAO
from Controller.CommentDAO import CommentDao
from Controller.PropertyAddonDAO import PropertyAddonDAO
from Controller.PropertyTypeDAO import PropertyTypeDAO
from Controller.UserDAO import UserDAO
from Controller.PropertyDAO import PropertyDAO
from Controller.BookingDAO import bookingDAO
from Controller.BillDAO import billDAO

def main():
    # Crear instancias de las clases DAO
    cardDAO = CardDAO()
    commentDAO = CommentDao()
    propertyAddonDAO = PropertyAddonDAO()
    propertyTypeDAO = PropertyTypeDAO()
    userDAO = UserDAO()
    propertyDAO = PropertyDAO()
    bookingDAo = bookingDAO()
    billDAo = billDAO()
    
    # Crear instancias de las clases VO
    propertyAddonVO = propertyAddon("","","","","","","","",)
    propertyTypeVO = propertyType("","")
    userVO = user("","","","","")
    propertyVO = property("","","","","","","","","","","","")
    bookingVO = Booking("","","","")
    billVO = bill("","","","","")
    commentVO = Comment("","","","","")
    cardVO = card("","","","","","","")

def signUpLogIn():
    print("Bienvenido a staycation")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    option = input("Seleccione una opción: ")

    userDAO = UserDAO()  # Crear una instancia de UserDAO

    if option == "1":
        user0 = user("", "", "", "", "")
        user0.userRole = input("Rol de usuario 1 si quiere ser administrador y 0 si quiere ser usuario: ")
        user0.name = input("Nombre: ")
        user0.email = input("Correo electrónico: ")
        user0.hashedPassword = input("Contraseña: ")
        user0.phone = input("Número de teléfono: ")
        userDAO.create_user(user0)  # Llamar al método create_user de la instancia

    elif option == "2":
        user0 = user("", "", "", "", "")
        user0.email = input("Correo electrónico: ")
        user0.hashedPassword = input("Contraseña: ")

        loggedInUser = userDAO.LogIn(user0)  # Llamar al método LogIn de la instancia
        if loggedInUser:
            print("Inicio de sesión exitoso")
        else:
            print("Correo electrónico o contraseña incorrectos")

    elif option == "3":
        print("Gracias por usar staycation")
        return
    else:
        print("Opción no válida")
        signUpLogIn()

def menuHost():
    print("Menú de anfitrión")
    print("1. Administrar propiedades")
    print("2. Adiministrar Reservas")
    print("3. Administrar comentarios")
    print("4. Administrar facturas")
    print("5. Cerrar sesión")
    option = input("Seleccione una opción: ")
    
    if option == "1":
        print("administración de propiedades")
        print("1. añadir propiedad")
        print("2. editar propiedad")
        print("3. eliminar propiedad")
        print("4. volver al menu principal")
        option = input("Seleccione una opción: ")
        if option == "1":
                pass
    if option == "2":
        print("administración de reservas")
        print("1. añadir reserva")
        print("2. editar reserva")
        print("3. eliminar reserva")
        print("4. volver al menu principal")
        option = input("Seleccione una opción: ")
    if option == "3":
        print("administración de comentarios")
        print("1. añadir comentario")
        print("2. editar comentario")
        print("3. eliminar comentario")
        print("4. volver al menu principal")
        option = input("Seleccione una opción: ")
    if option == "4":
        print("administración de facturas")
        print("1. añadir factura")
        print("2. editar factura")
        print("3. eliminar factura")
        print("4. volver al menu principal")
        option = input("Seleccione una opción: ")
    if option == "5":
        print("Gracias por usar staycation")
        return
    else:
        print("Opción no válida")
        menuHost()

def menuUser():
    print("Menú de usuario")
    print("1. Buscar propiedades")
    print("2. Reservar propiedad")
    print("3. Ver reservas")
    print("4. Ver facturas")
    print("5. Cerrar sesión")
    option = input("Seleccione una opción: ")
    
    if option == "1":
        print("Buscar propiedades")
        print("1. Buscar por tipo de propiedad")
        print("2. Buscar por servicios")
        print("3. Buscar por precio")
        print("4. Volver al menú principal")
        option = input("Seleccione una opción: ")
    if option == "2":
        print("Reservar propiedad")
        print("1. Reservar propiedad")
        print("2. Volver al menú principal")
        option = input("Seleccione una opción: ")
    if option == "3":
        print("Ver reservas")
        print("1. Ver reservas")
        print("2. Volver al menú principal")
        option = input("Seleccione una opción: ")
    if option == "4":
        print("Ver facturas")
        print("1. Ver facturas")
        print("2. Volver al menú principal")
        option = input("Seleccione una opción: ")
    if option == "5":
        print("Gracias por usar staycation")
        return
    else:
        print("Opción no válida")
        menuUser()


signUpLogIn()
