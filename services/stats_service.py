from models import Stats
from .users_service import UsersService


class StatsService:
    def __init__(self, users_service: UsersService):
        self.users_service = users_service

    def get_stats(self, principal) -> Stats:
        return Stats(
            total_users_number=self.users_service.get_total_number(principal),
        )
