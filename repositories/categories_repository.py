from models import Category
from .base_repository import BaseRepository
from models.translators import CategoryTranslator


class CategoriesRepository(BaseRepository):
    def __init__(
            self,
            collection,
            model_translator: CategoryTranslator,
            indexes,
    ):
        super().__init__(
            collection,
            model_translator,
            default_scope=[],
            indexes=indexes,
        )

    def find_by_name(self, name: str) -> Category | None:
        document = self.collection.find_one({"name": name})
        if not document:
            return None
        return self.model_translator.from_document(document)
