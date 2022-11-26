from app import app
from structure import structure
from faker import Faker
from repositories import UsersRepository
from tests.users_factory import UsersFactory


class TestUsersBlueprint:
    def setup_method(self):
        self.users_factory = UsersFactory()
        self.client = app.test_client()
        self.context = app.app_context()
        self.context.push()
        self.faker = Faker()
        self.users_repository: UsersRepository = structure.instantiate('users_repository')

    def teardown_method(self):
        self.context.pop()
        self.users_repository.delete_all()

    def test_create_user_creates_user(self):
        attrs = {
            "name": "test-name",
            "phone_number": "test-phone-number",
            "city": "test-city",
        }

        response = self.client.post(
            '/v1/users/create/',
            json=attrs,
        )
        assert response.status_code == 200
        assert response.json["id"]

    def test_get_all_users(self):
        expected_number_of_users = 5
        for i in range(expected_number_of_users):
            user = self.users_factory.generic()
            user.id = self.users_repository.create(user)

        response = self.client.get('/v1/users/')

        assert response.status_code == 200
        assert isinstance(response.json, list)
        for item in response.json:
            assert isinstance(item, dict)
        assert len(response.json) == expected_number_of_users
