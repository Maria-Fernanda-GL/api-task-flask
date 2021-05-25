from flask import Flask


def create_app(environment):
    from . import models, routes
    app = Flask(__name__)
    app.config.from_object(environment)

    with app.app_context():
        models.init_app(app)
        routes.init_app(app)

        # create tables in database
        models.db.create_all()

    return app
