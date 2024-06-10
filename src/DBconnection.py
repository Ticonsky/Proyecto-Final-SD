import mysql.connector
from mysql.connector import Error
import json
import os

class databaseConnection:
    def __init__(self):
        try:
            config_path = os.path.join(os.path.dirname(__file__), 'config.json')
            with open(config_path) as config_file:
                self.config = json.load(config_file)
        except Error as e:
            print(f"Error al cargar la configuración: {e}")
            self.config = None

    def getConnection(self):
        if self.config:
            try:
                conn = mysql.connector.connect(
                    host=self.config['host'],
                    database=self.config['database'],
                    user=self.config['user'],
                    password=self.config['password'],
                    port=self.config['port']
                )
                return conn
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
                return None
        else:
            raise Exception("Configuración no disponible")

    def getCursor(self, conn):
        if conn.is_connected():
            return conn.cursor()
        else:
            raise Exception("MySQL Connection not available")