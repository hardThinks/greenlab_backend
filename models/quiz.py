from bson import ObjectId
from .question import Question


class Quiz:
    def __init__(self):
        self.id: ObjectId | None = None
        self.name: str | None = None
        self.questions: list[Question] = []

    @staticmethod
    def from_request(attrs: dict) -> "Quiz":
        quiz = Quiz()
        quiz.name = attrs.get("name")
        return quiz
