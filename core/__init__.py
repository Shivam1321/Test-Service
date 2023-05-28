import hashlib
import json
from urllib.parse import unquote
from mongoengine import disconnect_all
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import (abort, Flask, request)

from core.config import (base_dir, BaseConfig)
from core.extra import db , login_manager


def reg_db(app):
    # disconnect_all()
    db.init_app(app)
    db.app = app



def reg_routes(app):
    from routers.user import users
    from routers.test import tests
    app.register_blueprint(users)
    app.register_blueprint(tests)
    
def reg_jwt(app):
    jwt = JWTManager(app)
    app.jwt_manager = jwt

def reg_auth(app):
    login_manager.init_app(app)
    login_manager.login_view = "users.login"


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class if config_class else BaseConfig)

    reg_db(app)
    reg_routes(app)
    reg_jwt(app)
    reg_auth(app)
   
    return app