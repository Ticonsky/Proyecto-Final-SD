import sys
import os

# Añadir el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.UserVO import user
from Model.PropertyVO import property
from Model.BookingVO import Booking
from Model.BillVO import bill
from Controller.UserDAO import UserDAO
from Controller.PropertyDAO import PropertyDAO
from Controller.BookingDAO import bookingDAO
from Controller.BillDAO import billDAO

def main():
    # Crear instancias de DAO
    user_dao = UserDAO()
    property_dao = PropertyDAO()
    booking_dao = bookingDAO()
    bill_dao = billDAO()

    # Crear un usuario
    new_user = user(userRole=1, name="John Doe", email="johndoe@example.com", password="password123", phone="1234567890")
    user_dao.create_user(new_user)
    
    # Crear una propiedad
    new_property = property(propertyId="1", location="123 Main St", name="Lovely Home", guests=4, rooms=2, beds=2, bathrooms=1, photos="photo.jpg", description="A lovely home", price=100.0, propertyTypeId="1", propertyAddonId="1")
    property_dao.create_property(new_property, new_user, new_property.propertyTypeId, new_property.propertyAddonId)
    
    # Crear una reserva
    check_in_date = "2024-06-01"
    check_out_date = "2024-06-07"
    new_booking = Booking(bookingId="1", userId=new_user.userId, propertyId=new_property.propertyId, startingDate=check_in_date, endingDate=check_out_date)
    booking_dao.create_booking(new_property, new_user, check_in_date, check_out_date)
    
    # Crear una factura
    bill_status = "Paid"
    new_bill = bill(billId="1", bookingId=new_booking.bookingId, propertyId=new_property.propertyId, propertyPrice=new_property.price, userId=new_user.userId, billStatus=bill_status)
    bill_dao.create_bill(new_booking, new_property, new_user, bill_status)
    
    # Obtener todas las facturas
    all_bills = bill_dao.get_all_bills()
    print("Todas las facturas:")
    for b in all_bills:
        print(b)
    
    # Obtener una factura específica
    specific_bill = bill_dao.get_bill_by_user_and_booking(new_user.userId, new_booking.bookingId)
    print("Factura específica:")
    print(specific_bill)

if __name__ == "__main__":
    main()
