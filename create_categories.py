from models import Category
from structure import structure
from repositories import CategoriesRepository
from time import sleep


def create_categories():
    repository: CategoriesRepository = structure.instantiate("categories_repository")
    categories = [
        Category(name="Системный аналитик"),
        Category(name="Аналитик-программист"),
        Category(name="Разработчик"),
        Category(name="Data engineer"),
        Category(name="Техническая поддержка"),
    ]

    for category in categories:
        if repository.find_by_name(category.name) is not None:
            continue
        repository.create(category)
    sleep(2)


if __name__ == '__main__':
    create_categories()
