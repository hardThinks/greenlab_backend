from typing import Any
from models import User


class UserTranslator:
    def __init__(self, quiz_result_translator):
        self.quiz_result_translator = quiz_result_translator

    def to_document(self, model: User) -> dict[str, Any]:
        return {
            "_id": model.id,
            "name": model.name,
            "phone_number": model.phone_number,
            "city": model.city,
            "quiz_results": [
                self.quiz_result_translator.to_document(item)
                for item in model.quiz_results
            ],
        }

    def from_document(self, document: dict[str, Any]) -> User:
        user = User()
        user.id = document.get("_id")
        user.name = document.get("name")
        user.phone_number = document.get("phone_number")
        user.city = document.get("city")
        user.quiz_results = [
            self.quiz_result_translator.from_document(item)
            for item in document.get("quiz_results")
        ]
        return user
