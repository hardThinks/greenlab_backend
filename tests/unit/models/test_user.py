from models import User


class TestUser:
    def test_from_request(self):
        request_args = {
            "name": "Test-name",
            "city": "Test-city",
            "phone_number": "Test-phone-number"
        }

        user = User.from_request(request_args)

        assert isinstance(user, User)
        assert user.id is None
        assert user.name == request_args["name"]
        assert user.phone_number == request_args["phone_number"]
        assert user.city == request_args["city"]

    def test_from_init(self):
        user = User()

        assert user.id is None
        assert user.name is None
        assert user.phone_number is None
        assert user.city is None
