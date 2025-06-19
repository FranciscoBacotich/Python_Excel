📊 Python Automation Toolkit for Excel & Data Workflows
Este repositorio contiene una colección de scripts y herramientas desarrolladas en Python para automatizar tareas repetitivas relacionadas con hojas de cálculo Excel, consultas a bases de datos SQL, manejo de archivos y notificaciones de escritorio.

El objetivo principal es ahorrar tiempo y reducir errores humanos al trabajar con grandes volúmenes de datos o tareas administrativas rutinarias.

🔧 Tecnologías y librerías utilizadas
pandas – Manipulación y análisis de datos

openpyxl / xlsxwriter – Lectura y escritura de archivos Excel

sqlalchemy – Conexión a bases de datos (MySQL, PostgreSQL, SQL Server)

pyodbc – Driver ODBC para conexión directa a SQL Server

plyer – Notificaciones de escritorio multiplataforma

schedule / task scheduler – Automatización de tareas programadas

dotenv – Manejo de variables de entorno y contraseñas seguras

⚙️ Funcionalidades principales
Exportación automática de resultados SQL a Excel

Aplicación de formatos personalizados en reportes (.xlsx)

Agendado de tareas mediante scripts o Task Scheduler

Envío de alertas visuales (notificaciones) tras la finalización de tareas

Organización del entorno con venv y requirements.txt

1) Crear Un venv para el proyecto : https://docs.python.org/3/library/venv.html
    python -m venv venv
    .\venv\Scripts\activate
    python --version

2) Setear un Jupyer Notebook : https://code.visualstudio.com/docs/datascience/jupyter-notebooks
    -Crear archivo ipynb o ejecutar script para abrirlo en navegador

3) Instalar pandas: https://pandas.pydata.org/docs/getting_started/install.html 
    -pip install pandas

   -For example, to install pandas with the optional dependencies to read Excel files.
    pip install "pandas[excel]"

4) Instalar dependencia openpyxl si es que no vino con el pip de install pandas
    -pip install openpyxl

5) Para crear un excel nuevo apartir de un df, aca decidimos usar: 
    -https://pypi.org/project/xlsxwriter/
    
