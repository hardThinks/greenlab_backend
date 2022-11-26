from faker import Faker
from models import User


class UsersFactory:
    faker = Faker()

    def generic(self) -> User:
        user = User()
        user.id = None
        user.name = self.faker.name()
        user.city = self.faker.city()
        user.phone_number = self.faker.phone_number()
        return user
