from .category import Category


class QuizResultItem:
    def __init__(self, category: Category, percentage: float):
        self.category = category
        self.percentage = percentage


class QuizResult:
    def __init__(self, quiz_result_items: list[QuizResultItem]):
        self.items = quiz_result_items
