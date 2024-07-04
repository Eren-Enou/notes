from flask import Flask
from .models import db
from .routes import home_bp, notes_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

        app.register_blueprint(home_bp)
        app.register_blueprint(notes_bp)

    return app
    