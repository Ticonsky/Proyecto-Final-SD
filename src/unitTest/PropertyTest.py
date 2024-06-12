import unittest
from unittest.mock import patch, MagicMock
from Model.PropertyVO import property
from Model.PropertyTypeVO import propertyType
from Model.PropertyAddonVO import propertyAddon
from Model.UserVO import user
from Controller.PropertyDAO import PropertyDAO

class TestPropertyDAO(unittest.TestCase):
    @patch('Model.DBconnetion.databaseConnection')
    def test_create_property(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        
        property_dao = PropertyDAO()
        test_property = property("123", "456", "789", "location", 4, 3, 2, 1, "photos", "Test Property", "A beautiful property", 100.0)
        test_user = user("userRole", "John Doe", "john.doe@example.com", "password123", "1234567890")
        test_property_type = propertyType("House", "A large house")
        test_property_addon = propertyAddon("S", "S", "S", "S", "S", "S", "S", "S")
        
        property_dao.create_property(test_property, test_user, test_property_type, test_property_addon)
        
        mock_cur.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

    @patch('Model.DBconnetion.databaseConnection')
    def test_getPropertyId(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchone.return_value = ("123",)
        
        property_dao = PropertyDAO()
        test_property = property("123", "456", "789", "location", 4, 3, 2, 1, "photos", "Test Property", "A beautiful property", 100.0)
        property_id = property_dao.getPropertyId(test_property)
        
        mock_cur.execute.assert_called_once_with("SELECT propertyId FROM property WHERE location = %s AND name = %s", 
                                                 (test_property.location, test_property.name))
        self.assertEqual(property_id, "123")
    
    @patch('Model.DBconnetion.databaseConnection')
    def test_getAllProperties(self, mock_db):
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_db.return_value.getConnection.return_value = mock_conn
        mock_conn.getCursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [("123", "Test Property", "A beautiful property", 100.0)]
        
        property_dao = PropertyDAO()
        properties = property_dao.getAllProperties()
        
        mock_cur.execute.assert_called_once_with("SELECT * FROM property")
        self.assertEqual(properties, [("123", "Test Property", "A beautiful property", 100.0)])

if __name__ == "__main__":
    unittest.main()
