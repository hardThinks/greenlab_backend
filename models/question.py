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


class Question:
    def __init__(self, value: str, weights: list[Weight]):
        self.id = None
        self.value = value
        self.weights = weights
