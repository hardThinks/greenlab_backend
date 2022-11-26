from typing import Any
from models import QuizResult


class QuizResultTranslator:
    def __init__(self, quiz_result_item_translator):
        self.quiz_result_item_translator = quiz_result_item_translator

    def to_document(self, quiz_result: QuizResult) -> dict[str, Any]:
        return {
            "items": [
                self.quiz_result_item_translator.to_document(item)
                for item in quiz_result.items
            ],
        }

    def from_document(self, document: dict) -> QuizResult:
        return QuizResult(
            quiz_result_items=[
                self.quiz_result_item_translator.from_document(item)
                for item in document.get("items")
            ],
        )
