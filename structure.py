from types import LambdaType

from dependencies import Dependencies

from services import PageService
from models.factories.mongo_index_factory import (
    MongoIndexFactory,
    MongoColumnFactory,
)

index_factory = MongoIndexFactory()
column_factory = MongoColumnFactory()


class Structure:
    def __init__(self, dependencies: Dependencies):
        self.dependencies = dependencies
        self.structure = {
            'page_service': {
                'class': PageService,
            },
        }

    def decorate_auth_handler(self, handler_key, policy):
        factory = self.instantiate('auth_decorator_factory')
        handler = self.instantiate(handler_key)
        return factory.decorate(handler, policy)

    def instantiate(self, key):
        if hasattr(self, key):
            return getattr(self, key)

        element = self.structure[key]
        result = None

        if isinstance(element, dict):
            args = [self.__instantiate_arg(arg) for arg in element.get('args', [])]
            kwargs = {}
            for key in element.get('kwargs', {}):
                kwargs[key] = self.__instantiate_arg(element['kwargs'][key])
            result = element['class'](*args, **kwargs)
        elif isinstance(element, LambdaType):
            result = element()

        setattr(self, key, result)

        return getattr(self, key)

    def __instantiate_arg(self, arg):
        if isinstance(arg, str):
            return self.instantiate(arg)
        elif isinstance(arg, LambdaType):
            return arg()
        elif isinstance(arg, list):
            return [self.instantiate(k) for k in arg]
        elif isinstance(arg, dict):
            value = {}
            for k in arg:
                value[k] = self.instantiate(arg[k])
            return value
        return None


deps = Dependencies()
structure = Structure(deps)
