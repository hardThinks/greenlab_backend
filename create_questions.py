from models import Question, Weight
from structure import structure
from time import sleep


def create_questions():
    categories_repository = structure.instantiate("categories_repository")
    questions_repository = structure.instantiate("questions_repository")

    category_sys_analysis = categories_repository.find_by_name("Аналитика")
    category_analysis_programmer = categories_repository.find_by_name("Аналитика-программирование")
    category_developer = categories_repository.find_by_name("Разработка")
    category_data_engineer = categories_repository.find_by_name("Data engineer")
    category_support = categories_repository.find_by_name("Тех. поддержка")

    questions = [
        Question(
            value="Вы легко находите общий язык с людьми?",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=-3,
                    no_weight=-4,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=2,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=-1,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=3,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=-2,
                    mostly_no_weight=-3,
                    no_weight=-4,
                ),
            ],
        ),



        Question(
            value="Вы выходите из себя или нервничаете если у вас не получается что-то объяснить собеседнику",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=-4,
                    mostly_yes_weight=-3,
                    dont_know_weight=0,
                    mostly_no_weight=4,
                    no_weight=5,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=-2,
                    mostly_yes_weight=-1,
                    dont_know_weight=0,
                    mostly_no_weight=1,
                    no_weight=2,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=-1,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=1,
                    no_weight=2,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=-1,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=1,
                    no_weight=2,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=-5,
                    mostly_yes_weight=-4,
                    dont_know_weight=-2,
                    mostly_no_weight=4,
                    no_weight=5,
                ),
            ],
        ),



        Question(
            value="Вам интересна математика и/или математическое моделирование?",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=1,
                    mostly_no_weight=0,
                    no_weight=-1,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=4,
                    mostly_yes_weight=3,
                    dont_know_weight=2,
                    mostly_no_weight=1,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=4,
                    mostly_yes_weight=3,
                    dont_know_weight=2,
                    mostly_no_weight=1,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=-1,
                    mostly_no_weight=-3,
                    no_weight=-4,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
            ],
        ),

        Question(
            value="Вам интересно анализировать информацию и приходить к необычным выводам?",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=1,
                    mostly_no_weight=0,
                    no_weight=-1,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=3,
                    mostly_no_weight=-3,
                    no_weight=-4,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=-1,
                    mostly_no_weight=-3,
                    no_weight=-4,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
            ],
        ),

        Question(
            value="Вы любите создавать/конструировать что-то новое?",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=3,
                    mostly_no_weight=2,
                    no_weight=1,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=-2,
                    no_weight=-3,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=-1,
                    mostly_no_weight=-2,
                    no_weight=-3,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=4,
                    mostly_yes_weight=3,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
            ],
        ),
        Question(
            value="Вы бы хотели знать несколько языков программирования?",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=2,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=-1,
                    mostly_no_weight=-2,
                    no_weight=-3,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=-1,
                    no_weight=-1,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=3,
                    mostly_no_weight=2,
                    no_weight=1,
                ),
            ],
        ),
        Question(
            value="Вы бы хотели создавать сайты?",
            weights=[
                Weight(
                    category_id=category_sys_analysis.id,
                    yes_weight=2,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_analysis_programmer.id,
                    yes_weight=2,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_developer.id,
                    yes_weight=5,
                    mostly_yes_weight=4,
                    dont_know_weight=0,
                    mostly_no_weight=2,
                    no_weight=1,
                ),
                Weight(
                    category_id=category_data_engineer.id,
                    yes_weight=2,
                    mostly_yes_weight=1,
                    dont_know_weight=0,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
                Weight(
                    category_id=category_support.id,
                    yes_weight=3,
                    mostly_yes_weight=2,
                    dont_know_weight=1,
                    mostly_no_weight=0,
                    no_weight=0,
                ),
            ],
        ),
    ]
    for question in questions:
        if questions_repository.find_by_value(question.value) is not None:
            continue
        questions_repository.create(question)
    sleep(2)


if __name__ == '__main__':
    create_questions()
