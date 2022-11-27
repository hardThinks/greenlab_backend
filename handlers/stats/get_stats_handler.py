from flask import Response, Request
from services import StatsService
from ..base_handler import BaseHandler


class GetStatsHandler(BaseHandler):
    def handle(self, request: Request, principal=None) -> Response:
        self.service: StatsService
        return self.execute(
            principal=principal,
            handler_function=self.service.get_stats,
        )
