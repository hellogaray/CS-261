# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 2 - Part 3
# Description: Stack ADT class by completing provided skeleton code in the file stack_da.py.
# Last revised: 10/21/2020

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack.
        """
        self.da.insert_at_index(self.size(), value)

    def pop(self) -> object:
        """
        Removes the top element from the stack and returns its value. If the stack is empty it raises a custom exception.
        """
        if self.size() == 0:
            raise StackException
        else:
            pop_value = self.da.get_at_index(self.size() - 1)
            self.da.remove_at_index(self.size() - 1)
            return pop_value

    def top(self) -> object:
        """
        Returns the value of the top element of the stack. If the stack is empty it raises a custom exception.
        """
        if self.size() == 0:
            raise StackException
        else:
            return self.da.get_at_index(self.size() - 1)


# BASIC TESTING
if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
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

    print("\n# top example 1")
    s = Stack()
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
