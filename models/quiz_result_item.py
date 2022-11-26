from models import Category


class QuizResultItem:
    def __init__(self, category: Category, percentage: float):
        self.category = category
        self.percentage = percentage
