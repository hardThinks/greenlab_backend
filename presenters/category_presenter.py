from models import Category


class CategoryPresenter:
    def present(self, principal, category: Category) -> dict[str, str]:
        return {
            'id': str(category.id),
            'name': category.name,
            'description': category.description,
        }
