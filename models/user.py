from .quiz_result import QuizResult
from bson import ObjectId


class User:
    def __init__(self):
        self.id: ObjectId | None = None
        self.name: str | None = None
        self.phone_number: str | None = None
        self.city: str | None = None
        self.quiz_results: list[QuizResult] = []

    @staticmethod
    def from_request(request_args: dict) -> "User":
        user = User()
        user.name = request_args.get("name")
        user.phone_number = request_args.get("phone_number")
        user.city = request_args.get("city")
        user.quiz_results = []
        return user
