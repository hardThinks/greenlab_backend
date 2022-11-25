from app import app
from structure import structure
from faker import Faker


class TestUsersBlueprint:
    def setup_method(self):
        self.client = app.test_client()
        self.context = app.app_context()
        self.context.push()
        self.faker = Faker()
        self.users_repository = structure.instantiate('users_repository')

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
        print(response, flush=True)
        assert response.status_code == 200
        assert response.json["id"]
