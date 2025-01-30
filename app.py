from flask import Flask
from flask_cors import CORS
from database import db, init_db
from routes import register_routes
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    jwt = JWTManager(app)
    init_db(app)
    register_routes(app)
    return app

    
if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=os.getenv('PORT'))