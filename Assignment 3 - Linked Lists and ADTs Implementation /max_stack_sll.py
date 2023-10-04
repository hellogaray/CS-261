# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment #3 - Part 2
# Description: Stack ADT class.


from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def is_empty(self) -> bool:
        """
        Return True is Maxstack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the MaxStack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.length()

    # ------------------------------------------------------------------ #

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack.
        """
        self.sll_val.add_front(value)  # Pushes value to the front using add_front method.
        if self.sll_max.is_empty():
            self.sll_max.add_front(value)
        if value >= self.sll_max.get_front():
            self.sll_max.add_front(value)  # Pushes value to the front using add_front method.
        if value < self.sll_max.get_front():
            self.sll_max.insert_at_index(1, value)  # Pushes value to the back using add_back method.

    def pop(self) -> object:
        """
        Removes the top element from the stack and returns its value.
        """
        if self.sll_val.is_empty():  # If Stack is empty raises exception.
            raise StackException()
        else:
            first_value = self.sll_val.get_front()  # Gets the first value using get_front method.
            self.sll_val.remove_front()  # Removes the first value using remove_front method.
            self.sll_max.remove(first_value)  # Removes the first value using remove_front method.
            return first_value

    def top(self) -> object:
        """
        Returns the value of the top element of the stack without removing it.
        """
        if self.sll_val.is_empty():  # If Stack is empty raises exception.
            raise StackException()
        else:
            return self.sll_val.get_front()  # Returns the first value using get_front method.

    def get_max(self) -> object:
        """
        Returns the maximum value currently stored in the stack.
        """
        if self.sll_val.is_empty():  # If Stack is empty raises exception.
            raise StackException()
        else:
            return self.sll_max.get_front()


# BASIC TESTING
if __name__ == "__main__":
    # pass

    print('\n# push example 1')
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print('\n# pop example 1')
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print('\n# top example 1')
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)

    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
