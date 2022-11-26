import math
from random import shuffle

from bson import ObjectId

from models import Category, QuizResultItem, QuizAnswerItem, PossibleAnswers
from repositories import QuestionsRepository, CategoriesRepository
from services import ValidatorService



class QuizService:
    def __init__(
            self,
            categories_repository: CategoriesRepository,
            questions_repository: QuestionsRepository,
            get_quiz_result_validator: ValidatorService,
    ):
        self.categories_repository = categories_repository
        self.questions_repository = questions_repository
        self.get_quiz_result_validator = get_quiz_result_validator

    def get_all_questions(self, principal) -> list[Category]:
        questions = self.questions_repository.get_list()
        shuffle(questions)
        return questions

    def get_quiz_result(self, attrs: dict, principal) -> list[QuizResultItem]:
        self.get_quiz_result_validator.validate(attrs)

        quiz_answers = self.__parse_quiz_answers(attrs)
        categories = self.categories_repository.get_list()
        category_to_max_points = {
            category: self.__count_max_points_for_category(category, quiz_answers)
            for category in categories
        }
        category_to_current_points = {
            category: self.__count_current_point_for_category(category, quiz_answers)
            for category in categories
        }
        quiz_result_items = []
        for category in categories:
            current_points = category_to_current_points.get(category)
            max_point = category_to_max_points.get(category)
            if current_points is None or not max_point:
                continue
            quiz_result_items.append(
                QuizResultItem(
                    category=category,
                    percentage=math.ceil(current_points / max_point * 100) % 101,
                ),
            )
        return quiz_result_items

    def __parse_quiz_answers(self, attrs: dict) -> list[QuizAnswerItem]:
        quiz_answers = []
        for item in attrs["result"]:
            question = self.questions_repository.find_by_id(item["question_id"])
            answer = item["answer"]
            quiz_answers.append(QuizAnswerItem(question, answer))
        return quiz_answers

    def __count_max_points_for_category(
            self,
            category: Category,
            quiz_answers: list[QuizAnswerItem],
    ) -> float:
        questions = [answer.question for answer in quiz_answers]
        points = 0
        for question in questions:
            weight = question.get_weight_by_category_id(category.id)
            if not weight:
                continue
            points += weight.max_weight
        return points if points > 0 else 0

    def __count_current_point_for_category(
            self,
            category: Category,
            quiz_answers: list[QuizAnswerItem],
    ) -> float:
        current_points = 0
        for quiz_answer in quiz_answers:
            weight = quiz_answer.question.get_weight_by_category_id(category.id)
            if not weight:
                continue
            if quiz_answer.answer == PossibleAnswers.YES.value:
                current_points += weight.yes_weight
            if quiz_answer.answer == PossibleAnswers.MOSTLY_YES.value:
                current_points += weight.mostly_yes_weight
            if quiz_answer.answer == PossibleAnswers.DONT_KNOW.value:
                current_points += weight.dont_know_weight
            if quiz_answer.answer == PossibleAnswers.NO.value:
                current_points += weight.no_weight
            if quiz_answer.answer == PossibleAnswers.MOSTLY_NO.value:
                current_points += weight.mostly_no_weight
        return current_points if current_points > 0 else 0
