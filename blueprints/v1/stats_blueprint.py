from flask import Blueprint, request
from flasgger import swag_from
from structure import structure
from handlers.stats import (
    GetStatsHandler,
)

stats_blueprint = Blueprint("stats_v1", __name__)
base_swagger_path = "./../../documentation/stats"


@stats_blueprint.route("/stats", methods=["GET"])
@swag_from(f'{base_swagger_path}/get_stats.yml')
def get_stats():
    handler: GetStatsHandler = structure.instantiate("get_stats_handler")
    return handler.handle(request)
