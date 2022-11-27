from structure import structure
from app import app
from tests.factories import UsersFactory


class TestStatsBlueprint:
    def setup_method(self):
        self.users_factory = UsersFactory()
        self.users_repository = structure.instantiate("users_repository")
        self.client = app.test_client()
        self.context = app.app_context()
        self.context.push()

    def teardown_method(self):
        self.users_repository.delete_all()

    def test_stats_blueprint(self):
        response = self.client.get("/v1/stats")

        assert response.status_code == 200
        assert response.json["total_users"] == 0

    def test_stats_blueprint_with_users(self):
        expected_users_number = 5
        for _ in range(expected_users_number):
            self.users_repository.create(self.users_factory.generic())

        response = self.client.get("/v1/stats")

        assert response.status_code == 200
        assert response.json["total_users"] == expected_users_number
