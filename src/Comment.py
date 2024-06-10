from DBconnection import databaseConnection
from Booking import Booking
from User import User

class Comment:
    def __init__(self, bookingId, userId, content, uploadDate, rating):
        self.commentId = None
        self.bookingId = bookingId
        self.userId = userId
        self.content = content
        self.uploadDate = uploadDate
        self.rating = rating

    @staticmethod
    def addComment():
        email = input("Ingrese el email del usuario: ")
        booking_id = input("Ingrese el ID de la reserva: ")
        content = input("Ingrese el contenido del comentario: ")
        rating = int(input("Ingrese la calificación (0-5): "))
        if rating < 0 or rating > 5:
            print("Calificación inválida. Debe estar entre 0 y 5.")
            return
        user_id = User.getUserId(email)
        if not user_id:
            print("Usuario no encontrado.")
            return
        booking = Booking.getBookingById(booking_id)
        if not booking:
            print("Reserva no encontrada.")
            return
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("""
                INSERT INTO comment (bookingId, userId, content, uploadDate, rating)
                VALUES (%s, %s, %s, NOW(), %s)
                """, (booking_id, user_id, content, rating))
            conn.commit()
            print("Comentario agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el comentario: {e}")
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def getCommentById(commentId):
        try:
            db = databaseConnection()
            conn = db.getConnection()
            if not conn:
                raise Exception("No se pudo establecer la conexión a la base de datos.")
            cur = db.getCursor(conn)
            cur.execute("SELECT * FROM comment WHERE commentId = %s", (commentId,))
            comment = cur.fetchone()
        except Exception as e:
            print(f"Error al obtener el comentario: {e}")
            comment = None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
        if comment:
            return comment
        else:
            print("Comentario no encontrado")
            return None