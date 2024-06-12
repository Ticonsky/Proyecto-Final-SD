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
    bookingDAO = bookingDAO()
    billDAO = billDAO()
        
    # Crear instancias de las clases VO (Value Objects)
    propertyAddonVO = propertyAddon("S", "S", "S", "S", "S", "S", "S", "S")
    propertyTypeVO = propertyType("Casa", "Una casa grande")
    userVO = user("Usuario", "John Doe", "john.doe@example.com", "password123", "1234567890")
    propertyVO = property("1", "Casa", "S", "Bogotá", 5, 3, 4, 2, "http://example.com/photos", "Mi Casa", "Una casa hermosa", 100.0)
    bookingVO = Booking("1", "1", "2023-01-01", "2023-01-05")
    billVO = bill("1", "1", 100.0, "1", "Pagado")
    commentVO = Comment("1", "1", "Muy buen lugar", "2023-01-06", 5)
    cardVO = card("1", "1234-5678-8765-4321", "John Doe", "12/25", "123", 500.0)

    # Ejemplos de inserciones
    # 1. Crear un usuario
    userDAO.create_user(userVO)

    # 2. Crear un tipo de propiedad
    propertyTypeDAO.create_propertyType(propertyTypeVO)

    # 3. Crear un complemento de propiedad
    propertyAddonDAO.setAllCombinations()  # Suponiendo que esta función inserta todas las combinaciones posibles

    # 4. Crear una propiedad
    propertyDAO.create_property(propertyVO, userVO, propertyTypeVO, propertyAddonVO)

    # 5. Crear una reserva
    bookingDAO.create_booking(propertyVO, userVO, bookingVO.startingDate, bookingVO.endingDate)

    # 6. Crear una factura
    billDAO.create_bill(bookingVO, propertyVO, userVO, billVO.billStatus)

    # 7. Crear un comentario
    commentDAO.create_comment(bookingVO, userVO, commentVO)

    # 8. Crear una tarjeta
    cardDAO.create_card(cardVO, userVO)

    # Mostrar los resultados de las inserciones
    print("Propiedades: ", propertyDAO.getAllProperties())
    print("Tipos de Propiedades: ", propertyTypeDAO.get_propertyType(propertyTypeVO))
    print("Complementos de Propiedades: ", propertyAddonDAO.get_propertyAddons(propertyAddonVO))
    user_id = userDAO.get_userID(userVO)
    print("ID de Usuario: ", user_id)

    # Verificar si el user_id existe en la tabla de usuarios antes de crear la propiedad
    if user_id:
        print("Creación de propiedad exitosa: ", propertyDAO.create_property(propertyVO, userVO, propertyTypeVO, propertyAddonVO))
    else:
        print("Error: Usuario no encontrado en la base de datos.")

if __name__ == "__main__":
    main()
