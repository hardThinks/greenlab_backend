from bson import ObjectId


class Category:
    def __init__(self, name: str):
        self.id: ObjectId | None = None
        self.name: str = name
