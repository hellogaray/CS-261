# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 7 - Sort
# Description: Function that receives a StaticArray and sorts its content in non-descending order. Sorting must be done
# ‘in place’, meaning the original input array will be modified.


from a1_include import *


def sa_sort(arr: StaticArray) -> None:
    """
    While current position and next position stay within range function will either move to next value to compare if
    the current value is less than or swap them if current value is greater than next and then set next position to
    current position + 1.
    """
    current_position = 0  # Set current_position to 0.
    next_position = 1  # Set next_position to 1.
    while current_position in range(0, StaticArray.size(arr)):
        while next_position < StaticArray.size(arr):
            if StaticArray.get(arr, current_position) > StaticArray.get(arr, next_position):
                """If the current value is less than the next value swap them."""
                save_current = StaticArray.get(arr, current_position)
                save_next = StaticArray.get(arr, next_position)
                StaticArray.set(arr, current_position, save_next)
                StaticArray.set(arr, next_position, save_current)
            if StaticArray.get(arr, current_position) <= StaticArray.get(arr, next_position):
                """If the current value is greater than the next value move to the next value to compare to current."""
                next_position += 1
        next_position = current_position + 1  # Sets next position to current + 1 to keep looping.
        current_position += 1  # Sets current position to + 1 to know when to stop looping.
    return


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [1, 0]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        sa_sort(arr)
        print(arr)
