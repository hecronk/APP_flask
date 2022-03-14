from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    return app
