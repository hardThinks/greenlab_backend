from app import app
from tests.users_factory import UsersFactory


class TestCategoriesBlueprint:
    def setup_method(self):
        self.users_factory = UsersFactory()
        self.client = app.test_client()
        self.context = app.app_context()
        self.context.push()

    def test_get_all_predefined_categories(self):
        response = self.client.get('/v1/categories/')
        assert response.status_code == 200
        assert isinstance(response.json, list)
        categories = [item["name"] for item in response.json]
        assert len(categories) == 5
        assert set(categories) == {
            "Аналитика",
            "Аналитика-программирование",
            "Разработка",
            "Data engineer",
            "Тех. поддержка",
        }
