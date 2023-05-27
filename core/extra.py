from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

async_mode = None

io = SocketIO(async_mode=async_mode)



db = MongoEngine()
