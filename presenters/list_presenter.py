from typing import Any

from models import User


class ListPresenter:
    def __init__(self, user_presenter):
        self.user_presenter = user_presenter

    def present(self, principal, users: list[User]) -> list[dict[str, Any]]:
        return [
            self.user_presenter.present(principal, user)
            for user in users
        ]
