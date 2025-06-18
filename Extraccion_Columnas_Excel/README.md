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

5) En este ejemplo queremos crear un excel nuevo apartir de un df entonces aca decidimos usar: 
    -https://pypi.org/project/xlsxwriter/
    