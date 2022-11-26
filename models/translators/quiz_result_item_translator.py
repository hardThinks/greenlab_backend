from typing import Any

from models import QuizResultItem


class QuizResultItemTranslator:
    def __init__(self, category_translator):
        self.category_translator = category_translator

    def to_document(self, quiz_result_item: QuizResultItem) -> dict[str, Any]:
        return {
            'category': self.category_translator.to_document(quiz_result_item.category),
            'percentage': quiz_result_item.percentage,
        }

    def from_document(self, document: dict[str, Any]) -> QuizResultItem:
        return QuizResultItem(
            category=self.category_translator.from_document(document.get("category")),
            percentage=document.get("percentage"),
        )
