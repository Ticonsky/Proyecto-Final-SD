# Importaciones necesarias de otros módulos del proyecto y bibliotecas estándar
from Model.BookingVO import Booking
from Model.UserVO import user
from Controller.BookingDAO import bookingDAO
from Controller.UserDAO import UserDAO
from Model.DBconnetion import databaseConnection
from Model.CommentVO import Comment

# Clase que maneja las operaciones de acceso a datos para los comentarios
class CommentDao():
    comment = Comment("", "", "", "", "")

    def __init__(self):
        # Constructor de la clase CommentDao
        self.bookingDAO = bookingDAO()  # DAO para manejar las operaciones de reservas
        self.userDAO = UserDAO()  # DAO para manejar las operaciones de usuarios

    # Método para crear un comentario
    def create_comment(self, booking: Booking, user: user, comment: Comment):
        # Obtener el ID del usuario
        userId_result = self.userDAO.get_userID(user)
        if userId_result is None:
            print("Usuario no encontrado")
            return
        userId = userId_result[0]  # Acceder al primer elemento de la tupla devuelta por fetchone()

        # Obtener el ID de la reserva
        bookingId = self.bookingDAO.get_booking_id(booking)
        if bookingId is None:
            print("Reserva no encontrada")
            return

        content = comment.content
        uploadDate = comment.uploadDate
        rating = comment.rating

        try:
            # Establecer la conexión a la base de datos
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos")

            cur = db.getCursor(conn)
            # Ejecutar la inserción del comentario en la base de datos
            cur.execute("""
                INSERT INTO comment (bookingId, userId, content, uploadDate, rating)
                VALUES (%s, %s, %s, %s, %s)
                """, (bookingId, userId, content, uploadDate, rating))

            conn.commit()
        except Exception as e:
            print(f"Error al crear el comentario: {e}")
        finally:
            # Cerrar el cursor y la conexión si están abiertos
            if conn.is_connected():
                cur.close()
                conn.close()
