import hashlib
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_login import current_user, login_required, login_user
from models.test import Mcq, Test
from flask import Blueprint
from routers.base import BaseRoute
tests = Blueprint('tests', __name__, url_prefix='/api/v1/tests')

@tests.route("/register", methods =["POST"])
@jwt_required()
def register():
    new_test = request.get_json()
    mcqs_test = new_test["mcqs"]
    passing_marks = new_test["passing_marks"]
    total_marks = new_test["total_marks"]
    temp_mcq_list = []
    for mcq in mcqs_test:
        temp_mcq = Mcq(question = mcq["question"], answers = mcq["answers"], right_answer = mcq["right_answer"], right_answer_index = mcq["right_answer_index"], marks_assigned = mcq["marks_assigned"])
        temp_mcq_list.append(temp_mcq)
    document = Test(mcqs=temp_mcq_list,passing_marks = passing_marks, total_marks = total_marks)
    document.save()
    return jsonify({'msg': 'Test created successfully'}) , 201


    
