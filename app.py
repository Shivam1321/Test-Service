
# import datetime
from flask import Flask, request, jsonify
# from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from mongoengine import connect
# from models import db
# from flask_restful import Api
# from core import create_app
# app = Flask(__name__)
# jwt = JWTManager(app)
# app.config['JWT_SECRET_KEY'] = 'SkilledBeingsTestService989$w'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# # db.init_app(app)
# CORS(app)

# api = Api(app)

from core import create_app
from core.config import BaseConfig
from core.extra import io

app = create_app(BaseConfig)
io.init_app(app)

@app.route('/api/v1/health', methods = ["GET"])
def health_check():
    print("Server health is good")
    return jsonify({'msg':"health good"})



if __name__ == '__main__':
	# app.run(host ="localhost", port= 9696)
    print("Server running on port 9696")
    io.run(app, debug=False, host='localhost', port=9696)
