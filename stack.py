

class Stack():
    """
    Stack data structure.
    """

    def __init__(self, size):
        """
        Initializes Stack object
        and set it's max size.
        """
        self.stack = [0 for x in range(size)]
        self.size = size
        self.current_index = 0

    def is_empty(self) -> bool:
        """
        Returns True if stack is empty.
        """
        return self.current_index == 0

    def top(self) -> int:
        """
        Returns top item in the stack.
        """
        if self.current_index >= 1:
            return self.stack[self.current_index-1]
        else:
            raise IndexError('Stack index out of range')

    def push(self, value):
        """
        Iserts item to the stack.
        """
        if self.current_index <= self.size-1:
            self.stack[self.current_index] = value
            self.current_index += 1
        else:
            raise IndexError('Stack index out of range')

    def pop(self) -> int:
        """
        Returns top item in the stack
        and removes it from the stack.
        If no items are in the stack
        returns None.
        """
        if not self.is_empty():
            self.current_index -= 1
            return self.stack[self.current_index]
        return None

    def from_str(self, value):
        """
        Takes string value and pushes
        each character to the stack.
        """
        for i in value:
            self.push(i)

class Calculator():
    """
    For calculating, converting
    mathematical expressions.
    """

    @staticmethod
    def is_num(value):
        """
        Returns True if given string
        is a number.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    @classmethod
    def convert(cls, expression) -> str:
        """
        Takes expression in infix notation
        as input and converts it to postfix.
        """
        operators = {'-': 0, '+': 0, '*': 1, '/': 1}
        stack = Stack(len(expression))
        expression = expression.split(' ')
        result = ''

        for element in expression:
            if Calculator.is_num(element):
                result += element + ' '
            elif element == '(':
                stack.push(element)
            elif element == ')':
                while True:
                    if stack.is_empty():
                        raise ValueError('Missing closing bracket')
                    if stack.top() == '(':
                        stack.pop()
                        break
                    else:
                        result += stack.pop() + ' '
            elif element in operators.keys():
                while (not stack.is_empty() and
                       stack.top() != '(' and
                       operators[stack.top()] > operators[element]):
                    result += stack.pop() + ' '
                stack.push(element)
            else:
                raise ValueError('Invaid character in expression')

        while not stack.is_empty():
            result += stack.pop() + ' '

        return result.strip()

    @classmethod
    def calculate(cls, expression) -> float:
        """
        Takes expression in postfix notation
        as input and calculates it's value.
        """
        stack = Stack(len(expression))
        expression = expression.split(' ')

        for element in expression:
            if Calculator.is_num(element):
                stack.push(element)
            elif element in ['+', '-', '*', '/']:
                val_1 = float(stack.pop())
                val_2 = float(stack.pop())
                if element == '+':
                    stack.push(val_2 + val_1)
                if element == '-':
                    stack.push(val_2 - val_1)
                if element == '*':
                    stack.push(val_2 * val_1)
                if element == '/':
                    stack.push(val_2 / val_1)
            else:
                raise ValueError('Invaid character in expression')

        return stack.pop()
