from Model.BookingVO import Booking
from Model.UserVO import user
from Controller.BookingDAO import bookingDAO
from Controller.UserDAO import UserDAO
from Model.DBconnetion import databaseConnection
from Model.CommentVO import Comment

class CommentDao():
    comment=Comment("","","","","")
    def __init__(self):
        self.bookingDAO = bookingDAO()
        self.userDAO = UserDAO()

    def create_comment(self, booking: Booking, user: user, comment):
        userId = self.userDAO.get_userID(user)
        if userId is None:
            print("Usuario no encontrado")
            return

        bookingId = self.bookingDAO.get_booking_id(booking)
        if bookingId is None:
            print("Reserva no encontrada")
            return
        content=Comment.content
        uploadTime=Comment.uploadDate
        rating=Comment.rating

        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO comment (bookingId, userId, content, uploadDate, rating)
                VALUES (%s, %s, %s, NOW())
                """, (bookingId, userId, comment, uploadTime, content, rating))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el comentario: {e}")
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()