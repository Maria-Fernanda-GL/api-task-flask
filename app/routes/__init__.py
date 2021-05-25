from .routes_tasks import task_bp
from .routes_users import user_bp
from .routes_swagger import swagger_bp


def init_app(app):
    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(swagger_bp)
