from .users import users_bp
from .auth import auth_bp
from .hydroponic_system import hydroponic_system_bp
from .plants import plant_bp

def register_routes(app):
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(hydroponic_system_bp)
    app.register_blueprint(plant_bp)