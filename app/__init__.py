from flask import Flask
from app.resources import product , inventory, orders
from flask_cors import CORS
from app.services.job import scheduler
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app=app, resources={r"*": {"origins": "*"}})

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

def init_app(config):

    app.config.from_object(config)

    product.api.init_app(app)
    inventory.api.init_app(app)
    orders.api.init_app(app)

    app.register_blueprint(product.main)
    app.register_blueprint(inventory.main)
    app.register_blueprint(orders.main)

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Access API'
        }
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    scheduler.init_app(app)
    scheduler.start()

    return app
