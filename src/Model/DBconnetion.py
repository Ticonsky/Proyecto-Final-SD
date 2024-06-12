# Importación de módulos necesarios para la conexión a la base de datos y manejo de archivos
import mysql.connector
from mysql.connector import Error
import json
import os

# Clase que maneja la conexión a la base de datos
class databaseConnection:
    def __init__(self):
        # Constructor de la clase databaseConnection
        try:
            # Construcción de la ruta al archivo de configuración
            config_path = os.path.join(os.path.dirname(__file__), 'config.json')
            # Apertura y lectura del archivo de configuración
            with open(config_path) as config_file:
                self.config = json.load(config_file)
        except Error as e:
            # Manejo de errores en la carga de la configuración
            print(f"Error al cargar la configuración: {e}")
            self.config = None

    def getConnection(self):
        # Método para obtener la conexión a la base de datos
        if self.config:
            try:
                # Establecimiento de la conexión a la base de datos utilizando la configuración cargada
                conn = mysql.connector.connect(
                    host=self.config['host'],
                    database=self.config['database'],
                    user=self.config['user'],
                    password=self.config['password'],
                    port=self.config['port']
                )
                return conn
            except Error as e:
                # Manejo de errores en la conexión a MySQL
                print(f"Error al conectar a MySQL: {e}")
                return None
        else:
            # Excepción lanzada si la configuración no está disponible
            raise Exception("Configuración no disponible")

    def getCursor(self, conn):
        # Método para obtener el cursor de la conexión
        if conn.is_connected():
            return conn.cursor()
        else:
            # Excepción lanzada si la conexión no está disponible
            raise Exception("MySQL Connection not available")
