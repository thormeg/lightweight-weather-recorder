"""Weather recorder."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from weather_recorder.config import Config


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from weather_recorder.main.routes import main
    from weather_recorder.errors.handlers import errors
    from weather_recorder.weather_charts.routes import weather_charts
    app.register_blueprint(main)
    app.register_blueprint(weather_charts)
    app.register_blueprint(errors)

    return app
