from flask import Response, Request

from services import CategoriesService
from ..base_handler import BaseHandler


class GetAllCategoriesHandler(BaseHandler):

    def handle(self, request: Request, principal=None) -> Response:
        self.service: CategoriesService
        return self.execute(
            principal=principal,
            handler_function=self.service.get_all,
        )
