from random import shuffle
from models import Category
from repositories import QuestionsRepository


class QuizService:
    def __init__(
            self,
            questions_repository: QuestionsRepository,
    ):
        self.questions_repository = questions_repository

    def get_all_questions(self, principal) -> list[Category]:
        questions = self.questions_repository.get_list()
        shuffle(questions)
        return questions
