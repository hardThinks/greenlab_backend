import math
from random import shuffle


from models import (
    Category,
    QuizResult,
    QuizResultItem,
    QuizAnswerItem,
    PossibleAnswers,
    Quiz,
)
from repositories import (
    QuestionsRepository,
    CategoriesRepository,
    QuizRepository,
)
from services import ValidatorService, UsersService


class QuizService:
    def __init__(
            self,
            categories_repository: CategoriesRepository,
            questions_repository: QuestionsRepository,
            quiz_repository: QuizRepository,
            get_quiz_result_validator: ValidatorService,
            create_quiz_validator: ValidatorService,
            users_service: UsersService,
    ):
        self.categories_repository = categories_repository
        self.questions_repository = questions_repository
        self.quiz_repository = quiz_repository
        self.get_quiz_result_validator = get_quiz_result_validator
        self.create_quiz_validator = create_quiz_validator
        self.users_service = users_service

    def create_quiz(self, attrs: dict, principal) -> Quiz:
        self.create_quiz_validator.validate(attrs)
        quiz = Quiz.from_request(attrs)
        quiz.id = self.quiz_repository.create(quiz)
        return quiz

    def get_all_questions(self, principal) -> list[Category]:
        questions = self.questions_repository.get_list()
        shuffle(questions)
        return questions

    def get_quiz_result(self, attrs: dict, principal) -> QuizResult:
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
        quiz_result = QuizResult(quiz_result_items)
        self.users_service.add_quiz_result(attrs["user_id"], quiz_result)
        return quiz_result

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
