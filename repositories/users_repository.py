from models import User
from .base_repository import BaseRepository
from models.translators import UserTranslator


class UsersRepository(BaseRepository):
    def __init__(
            self,
            collection,
            model_translator: UserTranslator,
            indexes,
    ):
        super().__init__(
            collection,
            model_translator,
            default_scope=[],
            indexes=indexes,
        )

    def find_by_phone_number(self, phone_number: str | None) -> User | None:
        if not phone_number:
            return None
        document = self.collection.find_one({"phone_number": phone_number})
        if not document:
            return None
        return self.model_translator.from_document(document)

    def get_total_users_number(self):
        return self.collection.count_documents({})
