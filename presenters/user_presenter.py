from typing import Any

from models import User


class UserPresenter:
    def present(self, principal, user: User) -> dict[str, Any]:
        return {
            'id': str(user.id),
            'name': user.name,
            'phone_number': user.phone_number,
            'city': user.city,
        }
