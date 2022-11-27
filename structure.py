from types import LambdaType

from dependencies import Dependencies

from handlers.users import (
    CreateUserHandler,
    GetAllUsersHandler,
)
from handlers.categories import (
    GetAllCategoriesHandler,
)
from handlers.quiz import (
    GetAllQuestionsHandler,
    FinishQuizHandler,
    CreateQuizHandler,
)
from handlers.stats import GetStatsHandler
from services import (
    PageService,
    UsersService,
    ValidatorService,
    CategoriesService,
    QuizService,
    StatsService,
)
from models.factories.mongo_index_factory import (
    MongoIndexFactory,
    MongoColumnFactory,
)
from models.translators import (
    UserTranslator,
    CategoryTranslator,
    QuestionTranslator,
    WeightsTranslator,
    QuizResultTranslator,
    QuizResultItemTranslator, QuizTranslator,
)
from repositories import (
    UsersRepository,
    CategoriesRepository,
    QuestionsRepository, QuizRepository,
)
from validators import PresenceValidator
from presenters import (
    UserPresenter,
    ListPresenter,
    CategoryPresenter,
    QuestionPresenter,
    QuizResultItemPresenter,
    QuizResultPresenter,
    StatsPresenter,
    QuizPresenter,
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
            'create_quiz_handler': {
                'class': CreateQuizHandler,
                'args': [
                    'quiz_service',
                    'quiz_presenter',
                ],
            },
            'quiz_presenter': {
                'class': QuizPresenter,
                'args': ['question_presenter'],
            },
            'get_stats_handler': {
                'class': GetStatsHandler,
                'args': [
                    'stats_service',
                    'stats_presenter',
                ],
            },
            'stats_presenter': {
                'class': StatsPresenter,
            },
            'stats_service': {
                'class': StatsService,
                'args': ['users_service'],
            },
            'finish_quiz_handler': {
                'class': FinishQuizHandler,
                'args': [
                    'quiz_service',
                    'quiz_result_presenter',
                ],
            },
            'quiz_result_presenter': {
                'class': QuizResultPresenter,
                'args': ["quiz_result_item_presenter"],
            },
            'categories_repository': {
                'class': CategoriesRepository,
                'args': [
                    lambda: self.dependencies.pymongo_wrapper().get_collection(
                        client=self.dependencies.mongo(),
                        collection_name='categories',
                    ),
                    'category_translator',
                    lambda: [],
                ],
            },
            'questions_repository': {
                'class': QuestionsRepository,
                'args': [
                    lambda: self.dependencies.pymongo_wrapper().get_collection(
                        client=self.dependencies.mongo(),
                        collection_name='questions',
                    ),
                    'question_translator',
                    lambda: [],
                ],
            },
            'quiz_service': {
                'class': QuizService,
                'args': [
                    'categories_repository',
                    'questions_repository',
                    'quiz_repository',
                    'get_quiz_result_validator_service',
                    'create_quiz_validator_service',
                    'users_service',
                ],
            },
            'quiz_repository': {
                'class': QuizRepository,
                'args': [
                    lambda: self.dependencies.pymongo_wrapper().get_collection(
                        client=self.dependencies.mongo(),
                        collection_name='quizzes',
                    ),
                    'quiz_translator',
                    lambda: [],
                ],
            },
            'quiz_translator': {
                'class': QuizTranslator,
                'args': ['question_translator'],
            },
            'create_quiz_validator_service': {
                'class': ValidatorService,
                'args': [
                    [
                        'name_presence_validator',
                    ],
                ],
            },

            'name_presence_validator': {
                'class': PresenceValidator,
                'args': [lambda: "name"],
            },
            'quiz_result_items_presenter': {
                'class': ListPresenter,
                'args': ['quiz_result_item_presenter'],
            },
            'quiz_result_item_presenter': {
                'class': QuizResultItemPresenter,
                'args': ['category_presenter'],
            },
            'get_quiz_result_validator_service': {
                'class': ValidatorService,
                'args': [
                    [
                        'quiz_result_presence_validator',
                        'user_id_presence_validator',
                    ],
                ],
            },
            'user_id_presence_validator': {
                'class': PresenceValidator,
                'args': [lambda: 'user_id'],
            },
            'quiz_result_presence_validator': {
                'class': PresenceValidator,
                'args': [lambda: 'result'],
            },
            'get_all_questions_handler': {
                'class': GetAllQuestionsHandler,
                'args': [
                    'quiz_service',
                    'questions_presenter',
                ],
            },
            'questions_presenter': {
                'class': ListPresenter,
                'args': ['question_presenter'],
            },
            'question_presenter': {
                'class': QuestionPresenter,
            },
            'question_translator': {
                'class': QuestionTranslator,
                'args': ['weights_translator'],
            },
            'weights_translator': {
                'class': WeightsTranslator,
            },
            'category_translator': {
                'class': CategoryTranslator,
            },
            'get_all_users_handler': {
                'class': GetAllUsersHandler,
                'args': [
                    'users_service',
                    'users_list_presenter',
                ],
            },
            'get_all_categories_handler': {
                'class': GetAllCategoriesHandler,
                'args': [
                    'categories_service',
                    'categories_list_presenter',
                ],
            },
            'categories_service': {
                'class': CategoriesService,
                'args': ['categories_repository'],
            },
            'categories_list_presenter': {
                'class': ListPresenter,
                'args': ['category_presenter'],
            },
            'category_presenter': {
                'class': CategoryPresenter,
            },
            'users_list_presenter': {
                'class': ListPresenter,
                'args': ['user_presenter'],
            },
            'create_user_handler': {
                'class': CreateUserHandler,
                'args': [
                    'users_service',
                    'user_presenter',
                ],
            },
            'user_presenter': {
                'class': UserPresenter,
                'args': [
                    'quiz_result_presenter',
                ],
            },
            'users_service': {
                'class': UsersService,
                'args': [
                    'users_repository',
                    'create_user_validator_service',
                ],
            },
            'users_repository': {
                'class': UsersRepository,
                'args': [
                    lambda: self.dependencies.pymongo_wrapper().get_collection(
                        client=self.dependencies.mongo(),
                        collection_name='users',
                    ),
                    'user_translator',
                    lambda: [],
                ],
            },
            'user_translator': {
                'class': UserTranslator,
                'args': [
                    'quiz_result_translator',
                ],
            },
            'quiz_result_translator': {
                'class': QuizResultTranslator,
                'args': [
                    'quiz_result_item_translator',
                ],
            },
            'quiz_result_item_translator': {
                'class': QuizResultItemTranslator,
                'args': [
                    'category_translator',
                ],
            },
            'create_user_validator_service': {
                'class': ValidatorService,
                'args': [
                    [
                        'user_name_presence_validator',
                        'user_phone_number_presence_validator',
                        'user_city_presence_validator',
                    ],
                ],
            },
            'user_name_presence_validator': {
                'class': PresenceValidator,
                'args': [lambda: 'name'],
            },
            'user_phone_number_presence_validator': {
                'class': PresenceValidator,
                'args': [lambda: 'phone_number'],
            },
            'user_city_presence_validator': {
                'class': PresenceValidator,
                'args': [lambda: 'city'],
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
