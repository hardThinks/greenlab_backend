import pytest

from infrastructure import InvalidRequestException
from models import User
from services import UsersService
from unittest.mock import Mock


class TestUsersService:
    def setup_method(self):
        self.users_repository_mock = Mock()
        self.create_validator_mock = Mock()
        self.service = UsersService(
            self.users_repository_mock,
            self.create_validator_mock,
        )

    def test_create_creates_new_user(self):
        attrs = {
            "name": "test-name",
            "phone_number": "test-phone-number",
            "city": "test-city",
        }
        created_id = Mock()

        self.users_repository_mock.find_by_phone_number.return_value = None
        self.users_repository_mock.create.return_value = created_id
        user = self.service.create(attrs, principal=None)

        assert isinstance(user, User)
        assert user.name == attrs["name"]
        assert user.phone_number == attrs["phone_number"]
        assert user.city == attrs["city"]
        assert user.id == created_id

    def test_create_raises_invalid_request_exception(self):
        attrs = {
            "name": "test-name",
            "phone_number": "test-phone-number",
            "city": "test-city",
        }

        self.users_repository_mock.find_by_phone_number.return_value = Mock()
        with pytest.raises(InvalidRequestException) as ex:
            self.service.create(attrs, principal=None)

        assert ex.value.errors == {"user": ["already_exists"]}
