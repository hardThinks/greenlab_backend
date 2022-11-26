from random import randint

from bson import ObjectId
from faker import Faker
from models import User, Category, QuizResult, QuizResultItem


class UsersFactory:
    @staticmethod
    def generic() -> User:
        faker = Faker()
        user = User()
        user.id = None
        user.name = faker.name()
        user.city = faker.city()
        user.phone_number = faker.phone_number()
        user.quiz_results = [QuizResultFactory.generic() for _ in range(3)]
        return user


class CategoriesFactory:
    @staticmethod
    def generic() -> Category:
        category = Category(name='test-category', description='test-description')
        category.id = ObjectId()
        return category


class QuizResultFactory:
    @staticmethod
    def generic() -> QuizResult:
        return QuizResult([QuizResulItemFactory.generic() for _ in range(3)])


class QuizResulItemFactory:
    @staticmethod
    def generic() -> QuizResultItem:
        return QuizResultItem(
            category=CategoriesFactory.generic(),
            percentage=randint(0, 100),
        )
