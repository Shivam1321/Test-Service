from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO
from flask_login import LoginManager
async_mode = None

io = SocketIO(async_mode=async_mode)

login_manager = LoginManager()


db = MongoEngine()
