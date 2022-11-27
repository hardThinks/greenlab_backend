from flask import Blueprint, request
from flasgger import swag_from
from structure import structure
from handlers.quiz import (
    GetAllQuestionsHandler,
    FinishQuizHandler,
)

quiz_blueprint = Blueprint("quiz_v1", __name__)
base_swagger_path = "./../../documentation/quiz"


@quiz_blueprint.route("/quiz/questions", methods=["GET"])
@swag_from(f'{base_swagger_path}/get_all_questions.yml')
def get_all():
    handler: GetAllQuestionsHandler = structure.instantiate("get_all_questions_handler")
    return handler.handle(request)


@quiz_blueprint.route("/quiz", methods=["POST"])
@swag_from(f'{base_swagger_path}/create_quiz.yml')
def create_quiz():
    handler: GetAllQuestionsHandler = structure.instantiate("create_quiz_handler")
    return handler.handle(request)


@quiz_blueprint.route("/quiz/finish", methods=["POST"])
@swag_from(f'{base_swagger_path}/finish_quiz.yml')
def finish_quiz():
    handler: FinishQuizHandler = structure.instantiate("finish_quiz_handler")
    return handler.handle(request)
