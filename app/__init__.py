from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from .model import configure as config_db
from .serializer import configure as config_ma


# Swagger UI route
SWAGGER_URL = '/swagger-ui'
API_URL = '/swagger'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../temp/teste.db'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .games import bp_games
    app.register_blueprint(bp_games)

    @app.route('/swagger')
    def get_swagger():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Flask CRUD API"
        return jsonify(swag)

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
