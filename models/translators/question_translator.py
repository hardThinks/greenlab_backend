from typing import Any

from models import Question


class QuestionTranslator:
    def __init__(self, weights_translator):
        self.weights_translator = weights_translator

    def to_document(self, question: Question) -> dict[str, Any]:
        return {
            "_id": question.id,
            "value": question.value,
            "weights": self.weights_translator.to_document(question.weights),
        }

    def from_document(self, document: dict[str, Any]) -> Question:
        question = Question(
            value=document.get("value"),
            weights=self.weights_translator.from_document(document.get("weights")),
        )
        question.id = document.get("_id")
        return question
