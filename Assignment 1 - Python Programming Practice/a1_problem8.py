# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 8 - Remove Duplicates
# Description: Function that receives a StaticArray where the elements are already in sorted order and returns a new
# StaticArray with duplicate values removed. Original array should not be modified.


from a1_include import *


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    It creates a new array based on the amount of unique values from the original array and then moves to placing those
    values in the new array.
    """
    position = 0  # Set position to 0.
    new_array_position = 0  # Set new_array_position to 0
    count = 1  # Sets count to 1, count will be used to calculate the size for the new array.
    new_array = None  # Creates new_array variable (set to None), will later be replaced.
    if StaticArray.size(arr) == 1:
        new_array = arr
        return new_array
    while position < StaticArray.size(arr) - 1:
        """Creates a new array using the amount of unique values in the original array."""
        if StaticArray.get(arr, position) == StaticArray.get(arr, position + 1):
            position += 1
        else:
            position += 1
            count += 1
        new_array = StaticArray(count)
    position = 0  # Resets position to 0 to start the next while loop.
    while position in range(0, StaticArray.size(arr) - 1):
        """Starts placing the values in the values in the new array."""
        if StaticArray.get(arr, position) != StaticArray.get(arr, position + 1):
            """Places the current and next in the array."""
            StaticArray.set(new_array, new_array_position, StaticArray.get(arr, position))
            new_array_position += 1
            position += 1
            StaticArray.set(new_array, new_array_position, StaticArray.get(arr, position))
        else:
            position += 1
    return new_array


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
