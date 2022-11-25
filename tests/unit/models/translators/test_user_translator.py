from unittest.mock import Mock
from models import User
from models.translators import UserTranslator


class TestUserTranslator:
    def setup_method(self):
        self.translator = UserTranslator()

    def test_to_document(self):
        user = User()
        user.id = Mock()
        user.name = "test-name"
        user.phone_number = "test-phone-number"
        user.city = "test-city"

        document = self.translator.to_document(user)

        assert isinstance(document, dict)
        assert document["_id"] == user.id
        assert document["name"] == user.name
        assert document["phone_number"] == user.phone_number
        assert document["city"] == user.city
        assert len(document.keys()) == 4

    def test_from_document(self):
        document = {
            "_id": Mock(),
            "name": "test-name",
            "phone_number": "test-phone-number",
            "city": "test-city",
        }

        user = self.translator.from_document(document)

        assert isinstance(user, User)
        assert user.id == document["_id"]
        assert user.name == document["name"]
        assert user.phone_number == document["phone_number"]
        assert user.city == document["city"]
