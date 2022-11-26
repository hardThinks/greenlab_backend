from bson import ObjectId


class Weight:
    def __init__(
            self,
            category_id: ObjectId,
            yes_weight: float,
            mostly_yes_weight: float,
            dont_know_weight: float,
            no_weight: float,
            mostly_no_weight: float,
    ):
        self.category_id = category_id
        self.yes_weight = yes_weight
        self.mostly_yes_weight = mostly_yes_weight
        self.dont_know_weight = dont_know_weight
        self.no_weight = no_weight
        self.mostly_no_weight = mostly_no_weight

    @property
    def max_weight(self):
        return max(
            [
                self.yes_weight,
                self.mostly_yes_weight,
                self.dont_know_weight,
                self.no_weight,
                self.mostly_no_weight,
            ],
        )


class Question:
    def __init__(self, value: str, weights: list[Weight]):
        self.id = None
        self.value = value
        self.weights = weights

    def get_weight_by_category_id(self, category_id: ObjectId) -> Weight | None:
        for weight in self.weights:
            if weight.category_id != category_id:
                continue
            return weight
