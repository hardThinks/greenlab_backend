from flask import Blueprint, request
from flasgger import swag_from
from structure import structure
from handlers.quiz import GetAllQuestionsHandler

quiz_blueprint = Blueprint("quiz_v1", __name__)
base_swagger_path = "./../../documentation/quiz"


@quiz_blueprint.route("/quiz/questions", methods=["GET"])
@swag_from(f'{base_swagger_path}/get_all_questions.yml')
def get_all():
    handler: GetAllQuestionsHandler = structure.instantiate("get_all_questions_handler")
    return handler.handle(request)
