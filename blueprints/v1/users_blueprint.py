from flask import Blueprint, request
from flasgger import swag_from
from structure import structure
from handlers.users import CreateUserHandler

users_blueprint = Blueprint("users_v1", __name__)
base_swagger_path = "./../../documentation/users"


@users_blueprint.route("/users/create/", methods=["POST"])
@swag_from(f'{base_swagger_path}/create_user.yml')
def create_user():
    handler: CreateUserHandler = structure.instantiate("create_user_handler")
    return handler.handle(request)
