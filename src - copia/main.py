from User import User
from Booking import Booking
from Property import Property
from Bill import Bill
from Comment import Comment
from Property_type import propertyType
from Property_Addons import propertyAddon
from DBconnection import databaseConnection
from datetime import datetime
import uuid


def Login():
    User.logIn()

def signUp():
    User.signUp()


def LoginOrSignUp():
    print("1. Iniciar sesión")
    print("2. Registrarse")
    option = input("Seleccione una opción: ")

    if option == "1":
        Login()
    elif option == "2":
        signUp()
    else:
        print("Opción inválida")  





def adminMenu():
    print("1. Agregar propiedad")
    print("2. Agregar tipo de propiedad")
    print("3. Agregar complemento de propiedad")
    print("4. Agregar comentario")
    print("5. Agregar factura")
    print("6. Salir")
    option = input("Seleccione una opción: ")

    if option == "1":
        Property.addProperty()
    elif option == "2":
        propertyType.addPropertyType()
    elif option == "3":
        propertyAddon.addPropertyAddon()
    elif option == "4":
        Comment.addComment()
    elif option == "5":
        Bill.addBill()
    elif option == "6":
        return
    else:
        print("Opción inválida")

def userMenu():
    print("1. Buscar propiedad")
    print("2. Reservar propiedad")
    print("3. Salir")
    option = input("Seleccione una opción: ")

    if option == "1":
        Property.searchProperty()
    elif option == "2":
        Booking.addBooking()
    elif option == "3":
        return
    else:
        print("Opción inválida")
