"""
Dispatches single step operations in correct order.
"""
import operator


class Dispatcher:
    """
    Dispatches single step operations according to given rules.

    Attributes:
        operations:
            Dictionary containing string representation of operators along with
            their callables.
    """

    def __init__(self):
        self.operations = {'**': operator.pow,
                           '*': operator.mul,
                           '/': operator.truediv,
                           '+': operator.add,
                           '-': operator.sub}
        self.operations.items()

    def dispatch(self, tokens: list) -> int:
        """
        Dispatches all the operations.

        Arguments:
            tokens:
                List containing all the tokens.

        Raises:
            ZeroDivisionError: Calculation requires dividing by zero, which
            makes small puppies die.

            InvalidExpressionException: Raised when expression contains stuff
            like ['2', '4'] or ['-', '/']

        Returns:
            Result of calculation.
        """
        while len(tokens) > 1:
            last_length = len(tokens)
            for rule in self.operations.items():
                try:
                    i = tokens.index(rule[0])
                    tokens[i] = str(
                        rule[1](int(tokens[i - 1]),
                                int(tokens[i + 1])))
                    del tokens[i - 1]
                    del tokens[i]
                except ValueError:
                    pass
            if len(tokens) is last_length:
                raise InvalidExpressionException
        return int(tokens[0])


class InvalidExpressionException(Exception):
    """
    Raised when expression contains stuff like ['2', '4'] or ['-', '/'].
    """
