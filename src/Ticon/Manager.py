import sys
import os

# Añadir el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.UserVO import user
from Controller.UserDAO import UserDAO
from Model.PropertyTypeVO import propertyType
from Controller.PropertyTypeDAO import PropertyTypeDAO
from Model.PropertyAddonVO import propertyAddon
from Controller.PropertyAddonDAO import PropertyAddonDAO
from Model.CardVO import card
from Controller.CardDAO import CardDAO

uservo=user("0","0","0","0","0",)
UserdAO=UserDAO()
print(UserdAO.get_userID(uservo))

