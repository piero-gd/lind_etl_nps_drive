from dotenv import load_dotenv
import os

load_dotenv()

# Función para obtener una variable de entorno con un valor predeterminado
def get_env_variable(key, default=None):
    return os.getenv(key, default)

# Obtener desde las variables de entorno
DB_CONNECTION_STRING = get_env_variable('DB_CONNECTION_STRING')
FILE_ID = get_env_variable('FILE_ID')
DB_TABLE_NAME = get_env_variable('DB_TABLE_NAME')
