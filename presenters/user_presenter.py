from typing import Any

from models import User


class UserPresenter:
    def __init__(self, quiz_result_presenter):
        self.quiz_result_presenter = quiz_result_presenter

    def present(self, principal, user: User) -> dict[str, Any]:
        return {
            'id': str(user.id),
            'name': user.name,
            'phone_number': user.phone_number,
            'city': user.city,
            'quiz_results': [
                self.quiz_result_presenter.present(principal, item)
                for item in user.quiz_results
            ],
        }
