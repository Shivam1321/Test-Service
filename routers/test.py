import hashlib
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_login import current_user, login_required, login_user
from models.test import Mcq, Test
from models.user_test import user_test
from flask import Blueprint
from routers.base import BaseRoute
from core.success import success_response_dict
tests = Blueprint('tests', __name__, url_prefix='/api/v1/tests')

@tests.route("/register", methods =["POST"])
@jwt_required()
def register():
    current_user = get_jwt_identity()
    new_test = request.get_json()
    mcqs_test = new_test["mcqs"]
    passing_marks = new_test["passing_marks"]
    total_marks = new_test["total_marks"]
    temp_mcq_list = []
    
    for index in range(len(mcqs_test)):
        mcq = mcqs_test[index]
        temp_mcq = Mcq(question_no = index,question = mcq["question"], answers = mcq["answers"], right_answer = mcq["right_answer"], right_answer_index = mcq["right_answer_index"], marks_assigned = mcq["marks_assigned"])
        temp_mcq_list.append(temp_mcq)
    document = Test(mcqs=temp_mcq_list,passing_marks = passing_marks, total_marks = total_marks)
    document.save()
    return jsonify({'msg': 'Test created successfully'}) , 201

@tests.route("/mcq-list", methods =["GET"])
@jwt_required()
def get_mcq_list():
    current_user = get_jwt_identity()
    print(current_user,"current_user")
    tests = Test.objects()
    # return_data = success_response_dict()
    # return_data['data'] = tests
    return jsonify({'msg': 'Test fetched successfully', 'data': tests}) , 201


@tests.route("/attempt-test", methods =["POST"])
@jwt_required()
def attempt():
    current_user = get_jwt_identity()
    new_test = request.get_json()
    answers_list = new_test["answers_list"]
    # passing_marks = new_test["passing_marks"]
    # total_marks = new_test["total_marks"]
    document = user_test(test_id = new_test["test_id"],user_id = current_user["id"],answers_list = answers_list)
    document.save()
    return jsonify({'msg': 'Test attempted successfully'}) , 201


