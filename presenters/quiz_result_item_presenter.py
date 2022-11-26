from typing import Any

from models import QuizResultItem
from presenters import CategoryPresenter


class QuizResultItemPresenter:
    def __init__(self, category_presenter: CategoryPresenter):
        self.category_presenter = category_presenter

    def present(self, principal, quiz_result_item: QuizResultItem) -> dict[str, Any]:
        return {
            "percentage": quiz_result_item.percentage,
            "category": self.category_presenter.present(
                principal,
                quiz_result_item.category,
            ),
        }
