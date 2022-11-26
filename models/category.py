from bson import ObjectId


class Category:
    def __init__(self, name: str, description: str | None = None):
        self.id: ObjectId | None = None
        self.name: str = name
        self.description: str | None = description
