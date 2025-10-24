import os
from flask import Flask
from variables import cargarvariables

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='template')
#app = Flask(__name__)

app.config.from_pyfile('settings.py')
cargarvariables()
  
import rutas_inicio

import rutas_upload

import rutas_verfichero

import rutas_skills

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)