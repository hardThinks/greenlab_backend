from services import UsersService
from structure import structure


class TestUsersService:
    def setup_method(self):
        self.service = structure.instantiate("users_service")

    def test_type(self):
        assert isinstance(self.service, UsersService)
