from models import Question


class QuestionPresenter:
    def present(self, principal, question: Question) -> dict[str, str]:
        return {
            'id': str(question.id),
            'value': question.value,
        }
