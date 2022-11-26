from unittest.mock import Mock

from bson import ObjectId

from models import User
from structure import structure
from tests.factories import UsersFactory


class TestUserTranslator:
    def setup_method(self):
        self.translator = structure.instantiate('user_translator')

    def test_to_document(self):
        user = UsersFactory.generic()

        document = self.translator.to_document(user)

        assert isinstance(document, dict)
        assert document["_id"] == user.id
        assert document["name"] == user.name
        assert document["phone_number"] == user.phone_number
        assert document["city"] == user.city
        assert isinstance(document["quiz_results"], list)
        assert len(document.keys()) == 5
        from pprint import pprint
        pprint(document)

    def test_from_document(self):
        document = {
            "_id": Mock(),
            "name": "test-name",
            "phone_number": "test-phone-number",
            "city": "test-city",
            'quiz_results': [
                {
                    'items': [
                        {
                            'category': {
                                '_id': ObjectId('6382662abf6c75560883348a'),
                                'description': 'test-description',
                                'name': 'test-category',
                            },
                            'percentage': 71,
                        },
                        {
                            'category': {
                                '_id': ObjectId('6382662abf6c75560883348b'),
                                'description': 'test-description',
                                'name': 'test-category',
                            },
                            'percentage': 45,
                        },
                    ],
                },
            ],
        }

        user = self.translator.from_document(document)

        assert isinstance(user, User)
        assert user.id == document["_id"]
        assert user.name == document["name"]
        assert user.phone_number == document["phone_number"]
        assert user.city == document["city"]
        assert user.quiz_results
