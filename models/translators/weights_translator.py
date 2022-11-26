from typing import Any

from models import Weight


class WeightsTranslator:
    def to_document(self, weights: list[Weight]) -> list[dict[str, Any]]:
        return [
            {
                "category_id": weight.category_id,
                "yes_weight": weight.yes_weight,
                "mostly_yes_weight": weight.mostly_yes_weight,
                "dont_know_weight": weight.dont_know_weight,
                "no_weight": weight.no_weight,
                "mostly_no_weight": weight.mostly_no_weight,
            }
            for weight in weights
        ]

    def from_document(self, document: list[dict[str, Any]]) -> list[Weight]:
        return [
            Weight(
                item.get("category_id"),
                item.get("yes_weight"),
                item.get("mostly_yes_weight"),
                item.get("dont_know_weight"),
                item.get("no_weight"),
                item.get("mostly_no_weight"),
            )
            for item in document
        ]
