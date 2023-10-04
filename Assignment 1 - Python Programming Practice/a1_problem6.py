# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 6 - Is Sorted?
# Description: Function that receives a StaticArray and returns an integer that describes whether the array is sorted.
# Method should return 1 if the array is sorted in strictly ascending order. It should return 2 if the list is sorted
# in strictly descending order. Otherwise the method should return 0.


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    """
    Using status (set as None) decides whether to set it at 0 (if values are not in ascending or descending order), at 1
    (if all values are ascending), or at 2 (if all values are descending).
    """
    position = 0  # Set the position to 0, the first value in the list.
    status = None  # Sets status to None.
    while position in range(0, StaticArray.size(arr) - 1):
        """Iterate through list and change status to 0, 1, or 2 depending on results."""
        if status is None:
            """If status is None change to 1 if position is less than next, 2 if greater than next, and 0 if equal."""
            if StaticArray.get(arr, position) < StaticArray.get(arr, position + 1):
                status = 1
            if StaticArray.get(arr, position) > StaticArray.get(arr, position + 1):
                status = 2
            if StaticArray.get(arr, position) == StaticArray.get(arr, position + 1):
                status = 0
        if status == 1:
            """If status is 1 keep as 1 if position is less than next and 0 if greater or equal."""
            if StaticArray.get(arr, position) < StaticArray.get(arr, position + 1):
                status = 1  # Sets status.
            if StaticArray.get(arr, position) >= StaticArray.get(arr, position + 1):
                status = 0  # Sets status and stays out of the if statements.
        if status == 2:
            """If status is 2 keep as 2 if position is greater than next and 0 if less or equal."""
            if StaticArray.get(arr, position) > StaticArray.get(arr, position + 1):
                status = 2  # Sets status.
            if StaticArray.get(arr, position) <= StaticArray.get(arr, position + 1):
                status = 0  # Sets status and stays out of the if statements.
        position += 1  # Continues checking.
    if StaticArray.size(arr) < 2:
        """If the array size is less than 2 then set status to 1."""
        status = 1  # Sets status.
    return status


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
