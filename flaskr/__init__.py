import os
from flask import Flask


def create_app(test_config=None):
    # Crea y configura la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Carga la configuración de la instancia, si existe y no está en testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carga la configuración de testing
        app.config.from_mapping(test_config)

    # Se asegura de que existe la carpeta de la instancia
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Crea una página simple que dice hola
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    from . import db
    db.init_app(app)

    return app
