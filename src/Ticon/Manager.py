import sys
import os

# Añadir el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.UserVO import user
from Controller.UserDAO import UserDAO

user0 = user("1", "1", "1", "1","1")
userdao = UserDAO()
userdao.create_user(user0)

