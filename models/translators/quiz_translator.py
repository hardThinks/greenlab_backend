from typing import Any

from models import Quiz


class QuizTranslator:
    def __init__(self, question_translator):
        self.question_translator = question_translator

    def to_document(self, quiz: Quiz) -> dict[str, Any]:
        return {
            "_id": quiz.id,
            "name": quiz.name,
            "questions": [
                self.question_translator.to_document(question)
                for question in quiz.questions
            ],
        }

    def from_document(self, document: dict[str, Any]) -> Quiz:
        quiz = Quiz()
        quiz.id = document.get("_id")
        quiz.name = document.get("name")
        quiz.questions = [
            self.question_translator.from_document(item)
            for item in document.get("questions", [])
        ]
        return quiz
