from typing import Any
from models import User


class UserTranslator:
    def to_document(self, model: User) -> dict[str, Any]:
        return {
            "_id": model.id,
            "name": model.name,
            "phone_number": model.phone_number,
            "city": model.city,
        }

    def from_document(self, document: dict[str, Any]) -> User:
        user = User()
        user.id = document.get("_id")
        user.name = document.get("name")
        user.phone_number = document.get("phone_number")
        user.city = document.get("city")
        return user
