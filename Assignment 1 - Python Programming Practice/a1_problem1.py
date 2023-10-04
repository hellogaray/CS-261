# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 1 - Min Max
# Description: Write a function that receives a one dimensional array of integers and returns a Python tuple with two
# values - minimum and maximum values in the input array. You may assume that the input array will contain only integers
# and will have at least one element. You do not need to check for those conditions.


from a1_include import *


def min_max(arr: StaticArray) -> ():
    """
    Finds the minimum and maximum in a given array.
    """
    position = 0  # Position in the array.
    max_n = StaticArray.get(arr, position)  # Max number will start with the first number in the array.
    min_n = StaticArray.get(arr, position)  # Min number will start with the first number in the array.
    for i in range(StaticArray.size(arr)):
        """
        Iterates through each object in the list trying to find the max and min values.
        """
        if StaticArray.get(arr, position) > max_n:
            max_n = StaticArray.get(arr, position)  # If the current value is greater than max_n, replace max_n.
        if StaticArray.get(arr, position) < min_n:
            min_n = StaticArray.get(arr, position)  # If the current value is less than max_n, replace max_n.
        position += 1  # Position is move one each time it iterates through the list.
    return min_n, max_n


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    arr = StaticArray(5)
    for i, value in enumerate([8, 7, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    # example 2
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    # example 3
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))
