from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
import sqlalchemy

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import Barcode

    # Check if the database needs to be initialized
    engine = sqlalchemy.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    inspector = sqlalchemy.inspect(engine)
    if not inspector.has_table("barcodes"):
        with app.app_context():
            db.drop_all()
            db.create_all()

            load_sample_data()  # Load sample data for demo purposes

            app.logger.info("Initialized the database!")
    else:
        app.logger.info("Database already contains the barcodes table.")

    return app


def load_sample_data():
    # Load data from sample_data.csv into the Barcode model
    from .models import Barcode

    csv_file_path = os.path.join(os.path.dirname(__file__), "sample_data.csv")

    with open(csv_file_path, "r") as csvfile:
        header = csvfile.readline().strip().split(",")
        for line in csvfile:
            values = line.strip().split(",")
            barcode_data = dict(zip(header, values))
            barcode = Barcode(**barcode_data)
            db.session.add(barcode)

    db.session.commit()
