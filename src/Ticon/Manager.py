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
    PropertyDAo = PropertyDAO()
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
            property0=property("","","","","","","","","","","","")
            user0=user("","","","","")
            propertyType0=propertyType("","")
            propertyAddon0=propertyAddon("","","","","","","","",)

            print("ingrese sus credenciales")
            user0.email=input("ingrese su correo electronico: ")
            user0.hashedPassword=input("ingrese su contraseña: ")

            
            print("ingerese el tipo de propiedad")
            propertyType0.name=input("ingrese el nombre del tipo de propiedad: ")
            
            print("ingrese el addon de la propiedad , S para agregar y N para no agregar")
            propertyAddon0.wifi=input("ingrese si tiene wifi: ")
            propertyAddon0.kitchen=input("ingrese si tiene cocina: ")
            propertyAddon0.parking=input("ingrese si tiene parqueadero: ")
            propertyAddon0.staffService=input("ingrese si tiene servicio de personal: ")
            propertyAddon0.pool=input("ingrese si tiene piscina: ")
            propertyAddon0.securityCameras=input("ingrese si tiene camaras de seguridad: ")
            propertyAddon0.laundry=input("ingrese si tiene lavanderia: ")
            propertyAddon0.gym=input("ingrese si tiene gimnasio: ")


            print("ingrese los datos de la propiedad")
            property0.location=input("ingrese la ubicación de la propiedad: ")
            property0.guests=input("ingrese la cantidad de huespedes: ")
            property0.rooms=input("ingrese la cantidad de habitaciones: ")
            property0.beds=input("ingrese la cantidad de camas: ")
            property0.bathrooms=input("ingrese la cantidad de baños: ")
            property0.photos=input("ingrese la url de las fotos: ")
            property0.name=input("ingrese el nombre de la propiedad: ")
            property0.description=input("ingrese la descripción de la propiedad: ")
            property0.price=input("ingrese el precio de la propiedad: ")
            
            PropertyDAo.create_property(property0, user0, propertyType0, propertyAddon0)  # Llamar al método create_property de la instancia

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
        print("4. Volver al menú principal")
        option = input("Seleccione una opción: ")
        if option=="1":
            Propertydao = PropertyDAO()
            Propertydao.getAllProperties()
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



        
cardDAO = CardDAO()
commentDAO = CommentDao()
propertyAddonDAO = PropertyAddonDAO()
propertyTypeDAO = PropertyTypeDAO()
userDAO = UserDAO()
propertyDAo = PropertyDAO()
bookingDAo = bookingDAO()
billDAo = billDAO()
    
    # Crear instancias de las clases VO
propertyAddonVO = propertyAddon("s","s","s","s","s","s","s","s",)
propertyTypeVO = propertyType("1","casa")
userVO = user("0","0","0","0","0")
propertyVO = property("2","2","2","2","2","2","2","2","2","2","2","2")
bookingVO = Booking("","","","")
billVO = bill("","","","","")
commentVO = Comment("","","","","")
cardVO = card("","","","","","","")


print(propertyDAo.getAllProperties())
print(propertyTypeDAO.get_propertyType(propertyTypeVO)) 
print(propertyAddonDAO.get_propertyAddons(propertyAddonVO))
user_id = userDAO.get_userID(userVO)
print(user_id)

# Verificar si el user_id existe en la tabla de usuarios antes de crear la propiedad
if user_id:
    print(propertyDAo.create_property(propertyVO, userVO, propertyTypeVO, propertyAddonVO))
else:
    print("Error: Usuario no encontrado en la base de datos.")