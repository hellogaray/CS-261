# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 3 - Reverse
# Description: Write a function that receives a StaticArray and reverses the order of the elements in the array.
# Reversal must be done ‘in place’, meaning the original input array will be modified.


from a1_include import *


def reverse(arr: StaticArray) -> None:
    """
    Receives a StaticArray and reverses the order of the elements in the array.
    """
    position = 0  # Set the position to 0, the first value in the list.
    last_position = StaticArray.size(arr)  # Sets last_position to the length of the array.
    while position < StaticArray.size(arr) / 2:
        """
        As long as position is not greater than half the length of the array it continues to swap values.
        Last position is decreased by one at the beginning of each iteration.
        Position is increased by one at the end of each iteration.  
        """
        last_position -= 1  # Last Position is decreased by one.
        current_value = StaticArray.get(arr, position)  # Stores the current value (array[position]).
        last_value = StaticArray.get(arr, last_position)  # Stores the last value (array[last_position]).
        StaticArray.set(arr, last_position, current_value)  # Sets the last position to the value of current_value.
        StaticArray.set(arr, position, last_value)  # Sets the position to the value of last_value.
        position += 1  # Position is increased by one.
    return arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 5)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
