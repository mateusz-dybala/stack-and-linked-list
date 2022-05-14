"""
Implementation of Linked list.
"""

class Node():
    """
    Node class for LinkedList
    """

    def __init__(self, value):
        """
        Initializes Node and sets it's value.
        """
        self.value = value
        self.next = None

    def has_next(self):
        """
        Returns True if Node is
        linked to the next node.
        """
        return self.next is not None


class LinkedList():
    """
    Singly linked list.
    """

    def __init__(self):
        """
        Initializes empty LinkedList
        """
        self.first = Node(None)
        self.current_node = self.first

    def append(self, value):
        """
        Links new node containg given value
        to the last node in LinkedList
        """
        if self.first.value is None:
            self.first.value = value
        else:
            node = self.first
            while node.has_next():
                node = node.next
            node.next = Node(value)

    def from_str(self, value):
        """
        Takes string value and appends
        each character as a Node to the LinkedList.
        """
        for i in value:
            self.append(i)

    def has_next(self):
        """
        Returns True if LinkedList has next Node.
        """
        return self.current_node.has_next()

    def get_next(self):
        """
        Returns value of next Node.
        If LinkedList does not have next Node
        returns value of the last Node.
        """
        node = self.current_node.value
        if self.current_node.has_next():
            self.current_node = self.current_node.next

        return node

    def reset_next(self):
        """
        Resets looping threw Node values.
        """
        self.current_node = self.first

    def preview(self):
        """
        Prints LinkedList.
        """
        node = self.first
        print('Linked list = [ ', end='')
        while node.has_next():
            print(node.value, end=', ')
            node = node.next
        print(node.value, ']')
