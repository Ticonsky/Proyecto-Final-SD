import unittest
from unittest.mock import patch, MagicMock
from Model.CardVO import card
from Model.UserVO import user
from Controller.CardDAO import CardDAO

class TestCardDAO(unittest.TestCase):
    @patch('Model.DBconnetion.databaseConnection')
    def test_create_card(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        
        card_dao = CardDAO()
        test_card = card("123", "1234-5678-8765-4321", "John Doe", "12/25", "123", 1000.0)
        test_user = user("userRole", "John Doe", "john.doe@example.com", "password123", "1234567890")
        
        card_dao.create_card(test_card, test_user)
        
        mock_cur.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
    
    @patch('Model.DBconnetion.databaseConnection')
    def test_delete_card(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        
        card_dao = CardDAO()
        test_card = card("123", "1234-5678-8765-4321", "John Doe", "12/25", "123", 1000.0)
        
        card_dao.delete_card(test_card.cardId)
        
        mock_cur.execute.assert_called_once_with("DELETE FROM cards WHERE cardId = %s", (test_card.cardId,))
        mock_conn.commit.assert_called_once()
    
    @patch('Model.DBconnetion.databaseConnection')
    def test_update_card(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        
        card_dao = CardDAO()
        test_card = card("123", "1234-5678-8765-4321", "John Doe", "12/25", "123", 1000.0)
        
        card_dao.update_card(test_card)
        
        mock_cur.execute.assert_called_once_with("""
            UPDATE cards SET userId = %s, cardNumber = %s, cardOwner = %s, dueDate = %s, cvv = %s, balance = %s
            WHERE cardId = %s
            """, (test_card.userId, test_card.cardNumber, test_card.cardOwner, test_card.dueDate, test_card.cvv, test_card.balance, test_card.cardId))
        mock_conn.commit.assert_called_once()
    
    @patch('Model.DBconnetion.databaseConnection')
    def test_get_cardID(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchone.return_value = ("123",)
        
        card_dao = CardDAO()
        test_user = user("userRole", "John Doe", "john.doe@example.com", "password123", "1234567890")
        card_id = card_dao.get_cardID("1234-5678-8765-4321", test_user)
        
        mock_cur.execute.assert_called_once_with("SELECT cardId FROM card WHERE cardNumber = %s AND userId = %s", 
                                                 ("1234-5678-8765-4321", test_user.userId))
        self.assertEqual(card_id, "123")

if __name__ == "__main__":
    unittest.main()
