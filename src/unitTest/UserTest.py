import sys
import os
import unittest
from unittest.mock import patch, MagicMock

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


class TestUserDAO(unittest.TestCase):
    @patch('Model.DBconnetion.databaseConnection')
    def test_create_user(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur

        user_dao = UserDAO()
        test_user = user("0", "John Doe", "john.doe@example.com", "password123", "1234567890")
        user_dao.create_user(test_user)

        mock_cur.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

    @patch('Model.DBconnetion.databaseConnection')
    def test_delete_user(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur

        user_dao = UserDAO()
        test_user = user("0", "John Doe", "john.doe@example.com", "password123", "1234567890")
        user_dao.delete_user(test_user)

        mock_cur.execute.assert_called_once_with("DELETE FROM user WHERE name = %s", (test_user.name,))
        mock_conn.commit.assert_called_once()

    @patch('Model.DBconnetion.databaseConnection')
    def test_upgrade_user(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur

        user_dao = UserDAO()
        test_user = user("0", "John Doe", "john.doe@example.com", "password123", "1234567890")
        user_dao.upgradeUser(test_user)

        mock_cur.execute.assert_called_once_with("UPDATE user SET userRole = %s WHERE name = %s", (1, test_user.name))
        mock_conn.commit.assert_called_once()

    @patch('Model.DBconnetion.databaseConnection')
    def test_get_userID(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchone.return_value = ("12345",)

        user_dao = UserDAO()
        test_user = user("0", "John Doe", "john.doe@example.com", "password123", "1234567890")
        user_id = user_dao.get_userID(test_user)

        mock_cur.execute.assert_called_once_with("SELECT userId FROM user WHERE email = %s", (test_user.email,))
        self.assertEqual(user_id, "12345")

    @patch('Model.DBconnetion.databaseConnection')
    def test_LogIn(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchone.return_value = ("12345",)

        user_dao = UserDAO()
        test_user = user("0", "John Doe", "john.doe@example.com", "password123", "1234567890")
        logged_in_user = user_dao.LogIn(test_user)

        mock_cur.execute.assert_called_once_with("SELECT * FROM user WHERE email = %s AND hashedPassword = %s", 
                                                 (test_user.email, UserDAO.hashpassword(test_user.hashedPassword)))
        self.assertEqual(logged_in_user, ("12345",))

    @patch('Model.DBconnetion.databaseConnection')
    def test_getUserRol(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchone.return_value = ("0",)

        user_dao = UserDAO()
        test_user = user("0", "John Doe", "john.doe@example.com", "password123", "1234567890")
        user_role = user_dao.getUserRol(test_user)

        mock_cur.execute.assert_called_once_with("SELECT userRole FROM user WHERE email = %s AND hashedPassword = %s", 
                                                 (test_user.email, UserDAO.hashpassword(test_user.hashedPassword)))
        self.assertEqual(user_role, ("0",))

    @patch('Model.DBconnetion.databaseConnection')
    def test_check_user_exists(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchone.return_value = (1,)

        user_dao = UserDAO()
        user_exists = user_dao.check_user_exists("12345")

        mock_cur.execute.assert_called_once_with("SELECT COUNT(*) FROM user WHERE userId = %s", ("12345",))
        self.assertTrue(user_exists)

if __name__ == "__main__":
    unittest.main()
