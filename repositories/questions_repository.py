from models import Category
from .base_repository import BaseRepository
from models.translators import QuestionTranslator


class QuestionsRepository(BaseRepository):
    def __init__(
            self,
            collection,
            model_translator: QuestionTranslator,
            indexes,
    ):
        super().__init__(
            collection,
            model_translator,
            default_scope=[],
            indexes=indexes,
        )

    def find_by_value(self, value: str) -> Category | None:
        document = self.collection.find_one({"value": value})
        if not document:
            return None
        return self.model_translator.from_document(document)
