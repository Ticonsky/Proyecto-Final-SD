
class Comment:
    def __init__(self, bookingId, userId, content, uploadDate, rating):
        self.commentId = None
        self.bookingId = bookingId
        self.userId = userId
        self.content = content
        self.uploadDate = uploadDate
        self.rating = rating
    def get_comment_id(self):
        return self.commentId

    def set_comment_id(self, commentId):
        self.commentId = commentId

    def get_booking_id(self):
        return self.bookingId

    def set_booking_id(self, bookingId):
        self.bookingId = bookingId

    def get_user_id(self):
        return self.userId

    def set_user_id(self, userId):
        self.userId = userId

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_upload_date(self):
        return self.uploadDate

    def set_upload_date(self, uploadDate):
        self.uploadDate = uploadDate

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating