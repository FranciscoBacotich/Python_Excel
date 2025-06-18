from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import datetime
from plyer import notification

from dotenv import load_dotenv 

load_dotenv()  # Carga variables desde el archivo .env

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS").replace("@", "%40")  # encode si usás caracteres especiales
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# ---------------------------------------
# Verifica los drivers disponibles (opcional para pyodbc, no necesario con SQLAlchemy)
# print(pyodbc.drivers())

# Verifica el nombre del host SQL si hace falta: SELECT @@SERVERNAME
# ---------------------------------------

# PostgreSQL: crear engine con SQLAlchemy
# Nota: la contraseña "ThatSenuaGuy@12248650" necesita que el "@" esté codificado como %40
# URL = 'postgresql://usuario:contraseña@host:puerto/basededatos'
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# ---------------------------------------
# Consultar una tabla o vista específica
# Supongamos que tenemos una base con muchas columnas, y preferimos limitar qué traemos
# Por ahora, traemos todo de una view llamada elden_weapons.build_summary
# ---------------------------------------

# Consulta SQL
sqlQuery = "SELECT * FROM elden_weapons.build_summary"

# Ejecutar consulta y cargar en DataFrame
df = pd.read_sql(sql=sqlQuery, con=engine)

#Export the data on the desktop
df.to_csv(os.environ["userprofile"] + "\\Desktop\ExportedDataPythonScript\\ExportedData_" + "SQL_OrderData_"+
          datetime.now().strftime("%d-%b-%Y %H%M%S") + ".csv", index = False)

#Mostrar Notificaion al usuario con pyler
notification.notify(title= "Report Status!!!",
                    message = f"La informacion a sido exitosamente guardada en Excel.\
                    \nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}", timeout = 10)

# Mostrar los primeros registros
print(df.head())

#Usamos un archivo bat para hacer que windows corra nuestro script. Esto es util para luego poder automatizar.
#Vamos a usar el Task Scheduler de windows, pero podria ser cualquiera. 
