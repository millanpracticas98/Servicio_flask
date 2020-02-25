Instalar la virtualenv si no lo esta ya:

pip install virtualenv

Iniciamos el entorno de pruebas y lo activamos:

virtualenv env
env\Scripts\activate    

Descargamos flask (así solo se indstala en el entorno virtual) y vemos todas sus dependencias:

pip install Flask
pip freeze

En el fichero env/Scripts/activate.bat añador las líneas:
set "FLASK_APP=run.py"
set "FLASK_ENV=development"


Para posibles errores:
If you are using powershell it does not works i dont know why please use cmd.exe since i use VScode editor it provide powershell as a terminal(ctrl+) by default so i was trying to run flask app on the powershell and it was giving me same response as you are getting

1) open cmd.exe (or if you are VSCode user like me simply write cmd on that terminal)

2) set FLASK_APP=run.py (without spaces, only for first run then it remember until restart of cmd)

3) flask run (or just flask will also work)

Luego ya se puede seguir trabajando con el PowerShell

Para poder ejecutarlo:
flask run     y si queremos recibir peticiones de otros ordenadores flask run --host 0.0.0.0

Si da el siguiente error(ModuleNotFoundError: No module named 'flask_wtf'):
    pip install flask-wtf