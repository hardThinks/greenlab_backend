from .base_repository import BaseRepository
from models.translators import QuizTranslator


class QuizRepository(BaseRepository):
    def __init__(
            self,
            collection,
            model_translator: QuizTranslator,
            indexes,
    ):
        super().__init__(
            collection,
            model_translator,
            default_scope=[],
            indexes=indexes,
        )
