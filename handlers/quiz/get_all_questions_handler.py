from flask import Response, Request

from services import QuizService
from ..base_handler import BaseHandler


class GetAllQuestionsHandler(BaseHandler):

    def handle(self, request: Request, principal=None) -> Response:
        self.service: QuizService
        return self.execute(
            principal=principal,
            handler_function=self.service.get_all_questions,
        )
