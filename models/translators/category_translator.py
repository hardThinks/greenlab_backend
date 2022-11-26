from typing import Any

from models import Category


class CategoryTranslator:
    def to_document(self, category: Category) -> dict[str, Any]:
        return {
            "_id": category.id,
            "name": category.name,
            "description": category.description,
        }

    def from_document(self, document: dict[str, Any]) -> Category:
        category = Category(
            document.get("name"),
            document.get("description"),
        )
        category.id = document.get("_id")
        return category
