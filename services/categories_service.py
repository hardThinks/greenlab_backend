from models import Category
from repositories import CategoriesRepository


class CategoriesService:
    def __init__(
            self,
            repository: CategoriesRepository,
    ):
        self.repository = repository

    def get_all(self, principal) -> list[Category]:
        return self.repository.get_list()
