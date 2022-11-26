from models import Question
from enum import StrEnum


class PossibleAnswers(StrEnum):
    YES = "yes"
    MOSTLY_YES = "mostly_yes"
    DONT_KNOW = "dont_know"
    NO = "no"
    MOSTLY_NO = "mostly_no"


class QuizAnswerItem:
    def __init__(self, question: Question, answer: str):
        self.question = question
        self.answer = answer
