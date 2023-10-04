# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 5 - Range
# Description: Function that receives two integers start and end and returns a StaticArray that contains consecutive
# values that begin at start and end at end (inclusive).


from a1_include import *


def sa_range(start: int, end: int) -> StaticArray:
    """
    Takes a two parameters, if the "start" parameter (first) is greater than the second one it reverses them, if not
    it takes them as is. It counts the number of digits in between + 1 to create the length that will be used for a new
    array using StaticArray(length) and then places each value in the array.
    """
    length = 0  # Sets the length for the new array to 0.
    if start > end:  # If the start is greater than the end.
        for i in range(end, start + 1):
            """Calculate the length based on the amount of values in between start and end."""
            length += 1
        new_array = StaticArray(length)  # Creates the new array using length.
        position = length - 1  # Starts position to place at length - 1.
        for i in range(end, start + 1):
            """Starts placing values in the new array from right to left."""
            StaticArray.set(new_array, position, i)
            position -= 1  # Position decreases.
    if start <= end:  # If the end is greater than the start.
        for i in range(start, end + 1):
            """Calculate the length based on the amount of values in between end and start."""
            length += 1
        new_array = StaticArray(length)  # Creates the new array using length.
        position = 0  # Starts position to place at 0.
        for i in range(start, end + 1):
            """Starts placing values in the new array from left to right."""
            StaticArray.set(new_array, position, i)
            position += 1  # Position increases.
    return new_array


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
