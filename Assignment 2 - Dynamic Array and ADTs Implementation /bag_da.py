# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 2 - Part 2
# Description: Bag ADT class by completing provided skeleton code in the file bag_da.py.
# Last revised: 10/21/2020

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag.
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the provided value object. Returns True if an object
        was removed, False otherwise.
        """
        for i in range(0, self.size()):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the bag that match the provided value object.
        """
        count = 0  # Tracks number of times the value was encountered.
        for i in range(0, self.size()):
            if self.da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the content of the bag.
        """
        for i in range(0, self.size()):  # Iterates through list removing the first element until there's none.
            self.da.remove_at_index(0)

    def equal(self, second_bag: object) -> bool:
        """
        Compares the content of the bag with the content of the second bag.
        Returns True if elements are the same regardless of order, false otherwise.
        TODO: Write this implementation
        """
        status = False  # Sets default status to False.
        if self.size() == 0 and second_bag.size() == 0:
            status = True
        if self.size() != second_bag.size():
            return status
        for i in range(0, self.size()):
            if self.count(self.da.get_at_index(i)) == second_bag.count(self.da.get_at_index(i)):
                status = True
            else:
                status = False
        return status


# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
