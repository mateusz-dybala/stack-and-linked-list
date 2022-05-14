from linked_list import LinkedList
from stack import *


def is_palindrome(value):
    """
    Returns True if given value is a palindrome,
    else False.
    """
    value = str(value)
    stack = Stack(len(value))
    stack.from_str(value)
    linked_list = LinkedList()
    linked_list.from_str(value)

    while linked_list.has_next():
        if stack.pop() != linked_list.get_next():
            return False

    return True


def main():
    c = Calculator()
    infix = '( 3 * 6 + 2 ) + ( 14 / 3 + 4 )'
    postfix = c.convert(infix)
    print(infix, '=', c.calculate(postfix))

    expression = 'reviver'
    print(expression, 'is palindrome:', is_palindrome(expression))    


if __name__ == '__main__':
    main()
