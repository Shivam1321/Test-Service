import hashlib
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_login import current_user, login_required, login_user
from models.user import User
from flask import Blueprint
from routers.base import BaseRoute
users = Blueprint('users', __name__, url_prefix='/api/v1/users')

@users.route("/register", methods=["POST"])
def register():
	
	new_user = request.get_json() # store the json body request
	print(new_user,"request")
	new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrpt password
	doc = User.objects(username= new_user["username"]) # check if user exist
	if not doc:
		temp = User(username=new_user["username"],email= new_user["email"],password = new_user["password"],)
		temp.save()
		return jsonify({'msg': 'User created successfully'}), 201
	else:
		return jsonify({'msg': 'Username already exists'}), 409



@users.route("/login", methods=["POST"])
def login():
	
	login_details = request.get_json() # store the json body request
	user_from_db = User.objects(username = login_details['username']).first()  # search for user in database
	print(repr(user_from_db),"user_from_db")
	if user_from_db:
		encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
		if encrpted_password == user_from_db.password:
			access_token = create_access_token(identity=user_from_db.username) # create jwt token
			return jsonify(access_token=access_token), 200

	return jsonify({'msg': 'The username or password is incorrect'}), 401



@users.route("/profile",methods=["GET"])
@jwt_required()
# @login_required
def profile():
	current_user = get_jwt_identity() # Get the identity of the current user
	user_from_db = User.objects(username = current_user).first()
	if user_from_db:
		# del user_from_db['_id'], user_from_db[0].password # delete data we don't want to return
		return jsonify({'profile' : user_from_db }), 200
	else:
		return jsonify({'msg': 'Profile not found'}), 404