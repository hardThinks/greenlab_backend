from flask import Blueprint, request
from flasgger import swag_from
from structure import structure
from handlers.categories import GetAllCategoriesHandler

categories_blueprint = Blueprint("categories_v1", __name__)
base_swagger_path = "./../../documentation/categories"


@categories_blueprint.route("/categories/", methods=["GET"])
@swag_from(f'{base_swagger_path}/get_all.yml')
def get_all():
    handler: GetAllCategoriesHandler = structure.instantiate("get_all_categories_handler")
    return handler.handle(request)
