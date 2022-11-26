from app import app
from tests.users_factory import UsersFactory
from structure import structure
from repositories import QuestionsRepository, UsersRepository
from models import PossibleAnswers


class TestCategoriesBlueprint:
    def setup_method(self):
        self.users_factory = UsersFactory()
        self.client = app.test_client()
        self.context = app.app_context()
        self.context.push()
        self.questions_repository: QuestionsRepository = structure.instantiate(
            'questions_repository')
        self.users_repository: UsersRepository = structure.instantiate(
            "users_repository")

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

    def test_finish_quiz_v1(self):
        user = self.users_factory.generic()
        user.id = self.users_repository.create(user)
        predefined_questions = [
            self.questions_repository.find_by_value("Вы легко находите общий язык с людьми?"),
            self.questions_repository.find_by_value("Вы выходите из себя или нервничаете если у вас не получается что-то 'объяснить собеседнику"),
            self.questions_repository.find_by_value("Вам интересна математика и/или математическое моделирование?"),
            self.questions_repository.find_by_value("Вам интересно анализировать информацию и приходить к необычным выводам?"),
            self.questions_repository.find_by_value("Вы любите создавать/конструировать что-то новое?"),
            self.questions_repository.find_by_value("Вы бы хотели знать несколько языков программирования?"),
            self.questions_repository.find_by_value("Вы бы хотели создавать сайты?"),
        ]

        body = {
            "user_id": str(user.id),
            "result": [
                {
                    "question_id": str(predefined_questions[0].id),
                    "answer": "yes",
                },
                {
                    "question_id": str(predefined_questions[1].id),
                    "answer": "mostly_yes",
                },
                {
                    "question_id": str(predefined_questions[2].id),
                    "answer": PossibleAnswers.NO.value,
                },
                {
                    "question_id": str(predefined_questions[3].id),
                    "answer": PossibleAnswers.NO.value,
                },
                {
                    "question_id": str(predefined_questions[4].id),
                    "answer": PossibleAnswers.YES.value,
                },
                {
                    "question_id": str(predefined_questions[5].id),
                    "answer": PossibleAnswers.DONT_KNOW.value,
                },
                {
                    "question_id": str(predefined_questions[6].id),
                    "answer": "mostly_yes",
                },
            ],
        }

        response = self.client.post('/v1/quiz/finish', json=body)

        assert response.status_code == 200
        assert response.json[0]["percentage"] == 24
        assert response.json[1]["percentage"] == 12
        assert response.json[2]["percentage"] == 49
        assert response.json[3]["percentage"] == 4
        assert response.json[4]["percentage"] == 34


    def test_finish_quiz_v2(self):
        user = self.users_factory.generic()
        user.id = self.users_repository.create(user)
        predefined_questions = [
            self.questions_repository.find_by_value("Вы легко находите общий язык с людьми?"),
            self.questions_repository.find_by_value("Вы выходите из себя или нервничаете если у вас не получается что-то 'объяснить собеседнику"),
            self.questions_repository.find_by_value("Вам интересна математика и/или математическое моделирование?"),
            self.questions_repository.find_by_value("Вам интересно анализировать информацию и приходить к необычным выводам?"),
            self.questions_repository.find_by_value("Вы любите создавать/конструировать что-то новое?"),
            self.questions_repository.find_by_value("Вы бы хотели знать несколько языков программирования?"),
            self.questions_repository.find_by_value("Вы бы хотели создавать сайты?"),
        ]

        body = {
            "user_id": str(user.id),
            "result": [
                {
                    "question_id": str(predefined_questions[0].id),
                    "answer": PossibleAnswers.NO.value,
                },
                {
                    "question_id": str(predefined_questions[1].id),
                    "answer": "mostly_yes",
                },
                {
                    "question_id": str(predefined_questions[2].id),
                    "answer": "mostly_yes",
                },
                {
                    "question_id": str(predefined_questions[3].id),
                    "answer": PossibleAnswers.YES.value,
                },
                {
                    "question_id": str(predefined_questions[4].id),
                    "answer": PossibleAnswers.MOSTLY_NO.value,
                },
                {
                    "question_id": str(predefined_questions[5].id),
                    "answer": PossibleAnswers.NO.value,
                },
                {
                    "question_id": str(predefined_questions[6].id),
                    "answer": PossibleAnswers.MOSTLY_NO.value,
                },
            ],
        }

        response = self.client.post('/v1/quiz/finish', json=body)

        assert response.status_code == 200
        assert response.json[0]["percentage"] == 0
        assert response.json[1]["percentage"] == 16
        assert response.json[2]["percentage"] == 14
        assert response.json[3]["percentage"] == 34
        assert response.json[4]["percentage"] == 0



    def test_finish_quiz_v3(self):
        user = self.users_factory.generic()
        user.id = self.users_repository.create(user)
        predefined_questions = [
            self.questions_repository.find_by_value("Вы легко находите общий язык с людьми?"),
            self.questions_repository.find_by_value("Вы выходите из себя или нервничаете если у вас не получается что-то 'объяснить собеседнику"),
            self.questions_repository.find_by_value("Вам интересна математика и/или математическое моделирование?"),
            self.questions_repository.find_by_value("Вам интересно анализировать информацию и приходить к необычным выводам?"),
            self.questions_repository.find_by_value("Вы любите создавать/конструировать что-то новое?"),
            self.questions_repository.find_by_value("Вы бы хотели знать несколько языков программирования?"),
            self.questions_repository.find_by_value("Вы бы хотели создавать сайты?"),
        ]

        body = {
            "user_id": str(user.id),
            "result": [
                {
                    "question_id": str(predefined_questions[0].id),
                    "answer": PossibleAnswers.YES.value,
                },
                {
                    "question_id": str(predefined_questions[1].id),
                    "answer": PossibleAnswers.YES.value,
                },
                {
                    "question_id": str(predefined_questions[2].id),
                    "answer": PossibleAnswers.NO.value,
                },
                {
                    "question_id": str(predefined_questions[3].id),
                    "answer": PossibleAnswers.DONT_KNOW.value,
                },
                {
                    "question_id": str(predefined_questions[4].id),
                    "answer": PossibleAnswers.DONT_KNOW.value,
                },
                {
                    "question_id": str(predefined_questions[5].id),
                    "answer": PossibleAnswers.MOSTLY_NO.value,
                },
                {
                    "question_id": str(predefined_questions[6].id),
                    "answer": PossibleAnswers.YES.value,
                },
            ],
        }

        response = self.client.post('/v1/quiz/finish', json=body)

        assert response.status_code == 200
        assert response.json[0]["percentage"] == 24
        assert response.json[1]["percentage"] == 20
        assert response.json[2]["percentage"] == 21
        assert response.json[3]["percentage"] == 0
        assert response.json[4]["percentage"] == 19


