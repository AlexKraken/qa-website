from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import Barcode

    #with app.app_context():
    #    db.create_all()

    # Check if the database needs to be initialized
    engine = SQLAlchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = SQLAlchemy.inspect(engine)
    if not inspector.has_table("barcodes"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info('Initialized the database!')
    else:
        app.logger.info('Database already contains the barcodes table.')

    
    return app
