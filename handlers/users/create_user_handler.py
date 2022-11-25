from flask import Response, Request

from services import UsersService
from ..base_handler import BaseHandler


class CreateUserHandler(BaseHandler):

    def handle(self, request: Request, principal=None) -> Response:
        self.service: UsersService
        return self.execute(
            principal=principal,
            handler_function=self.service.create,
            attrs=request.json,
        )
