from flask import Flask

from config import Config
from app.controllers.home_controller import home_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(home_bp)
    return app
