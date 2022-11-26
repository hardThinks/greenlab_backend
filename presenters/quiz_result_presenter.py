from models import QuizResult


class QuizResultPresenter:
    def __init__(self, quiz_result_item_presenter):
        self.quiz_result_item_presenter = quiz_result_item_presenter

    def present(self, principal, quiz_result: QuizResult):
        return {
            "quiz_result_items": [
                self.quiz_result_item_presenter.present(principal, item)
                for item in quiz_result.items
            ],
        }
