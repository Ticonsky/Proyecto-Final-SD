# Clase que representa un comentario de usuario
class Comment:
    def __init__(self, bookingId, userId, content, uploadDate, rating):
        # Constructor de la clase Comment, inicializa los atributos del comentario
        self.commentId = None  # Identificador único del comentario, inicialmente None
        self.bookingId = bookingId  # Identificador de la reserva asociada al comentario
        self.userId = userId  # Identificador del usuario que realiza el comentario
        self.content = content  # Contenido del comentario
        self.uploadDate = uploadDate  # Fecha de publicación del comentario
        self.rating = rating  # Calificación otorgada en el comentario
    
    # Métodos getter y setter para cada atributo de la clase Comment

    # Getter para commentId
    def get_comment_id(self):
        return self.commentId

    # Setter para commentId
    def set_comment_id(self, commentId):
        self.commentId = commentId

    # Getter para bookingId
    def get_booking_id(self):
        return self.bookingId

    # Setter para bookingId
    def set_booking_id(self, bookingId):
        self.bookingId = bookingId

    # Getter para userId
    def get_user_id(self):
        return self.userId

    # Setter para userId
    def set_user_id(self, userId):
        self.userId = userId

    # Getter para content
    def get_content(self):
        return self.content

    # Setter para content
    def set_content(self, content):
        self.content = content

    # Getter para uploadDate
    def get_upload_date(self):
        return self.uploadDate

    # Setter para uploadDate
    def set_upload_date(self, uploadDate):
        self.uploadDate = uploadDate

    # Getter para rating
    def get_rating(self):
        return self.rating

    # Setter para rating
    def set_rating(self, rating):
        self.rating = rating
