from app import app
from tests.users_factory import UsersFactory


class TestCategoriesBlueprint:
    def setup_method(self):
        self.users_factory = UsersFactory()
        self.client = app.test_client()
        self.context = app.app_context()
        self.context.push()

    def test_get_all_predefined_questions(self):
        response = self.client.get('/v1/quiz/questions')

        assert response.status_code == 200
        assert isinstance(response.json, list)
        questions = [item["value"] for item in response.json]
        assert len(questions) == 7
        assert set(questions) == {
            "Вы легко находите общий язык с людьми?",
            "Вы выходите из себя или нервничаете если у вас не получается что-то 'объяснить собеседнику",
            "Вам интересна математика и/или математическое моделирование?",
            "Вам интересно анализировать информацию и приходить к необычным выводам?",
            "Вы любите создавать/конструировать что-то новое?",
            "Вы бы хотели знать несколько языков программирования?",
            "Вы бы хотели создавать сайты?",
        }
