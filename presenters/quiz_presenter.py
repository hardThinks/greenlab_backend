from typing import Any

from models import Quiz


class QuizPresenter:
    def __init__(self, question_presenter):
        self.question_presenter = question_presenter

    def present(self, principal, quiz: Quiz) -> dict[str, Any]:
        return {
            "id": str(quiz.id),
            "name": quiz.name,
            "questions": [
                self.question_presenter.present(principal, question)
                for question in quiz.questions
            ],
        }
