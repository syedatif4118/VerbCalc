import random

class CustomAnswers:
    def __init__(self) -> None:
        self._answers = ['It is', 'The answer is', 'The result is', 'The total is', 'Altogether you get']
        self._default = 'The result is'

    def get_phrase(self, default:bool = False):
        return self._answers[random.randrange(0, len(self._answers))] if not default else self._default
