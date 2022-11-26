from infrastructure.exceptions import InvalidRequestException
from repositories import UsersRepository
from models import User, QuizResult
from .validator_service import ValidatorService


class UsersService:
    def __init__(
            self,
            users_repository: UsersRepository,
            create_validator: ValidatorService,
    ):
        self.users_repository = users_repository
        self.create_validator = create_validator

    def create(self, attrs: dict, principal) -> User:
        self.create_validator.validate(attrs)
        user = User.from_request(attrs)
        stored_user = self.users_repository.find_by_phone_number(user.phone_number)
        if stored_user is not None:
            raise InvalidRequestException(errors={"user": ["already_exists"]})
        user.id = self.users_repository.create(user)
        return user

    def get_all(self, principal) -> list[User]:
        return self.users_repository.get_list()

    def add_quiz_result(self, user_id: str, quiz_result: QuizResult) -> None:
        user = self.users_repository.find_by_id(user_id)
        if not user:
            return
        user.quiz_results.append(quiz_result)
        self.users_repository.update(user)
