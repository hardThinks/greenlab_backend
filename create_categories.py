from models import Category
from structure import structure
from repositories import CategoriesRepository
from time import sleep


def create_categories():
    repository: CategoriesRepository = structure.instantiate("categories_repository")
    categories = [
        Category(name="Аналитика", description="Системный аналитик"),
        Category(name="Аналитика-программирование", description="1С, SAP Business Intelligence"),
        Category(name="Разработка", description="Web, JavaScript, 1С"),
        Category(name="Data engineer"),
        Category(name="Тех. поддержка"),
    ]

    for category in categories:
        if repository.find_by_name(category.name) is not None:
            continue
        repository.create(category)
    sleep(2)


if __name__ == '__main__':
    create_categories()
