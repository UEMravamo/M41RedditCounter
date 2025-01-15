from dotenv import load_dotenv
import os


# Carga de las variables del Archivo ".env"
load_dotenv()

CONFIG = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "user_agent": os.getenv("USER_AGENT"),
}

# Validación de Variables de Entorno
if not all(CONFIG.values()):
    raise EnvironmentError("Variables de entorno no configuradas correctamente.")
