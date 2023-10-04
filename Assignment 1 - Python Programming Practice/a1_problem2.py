# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 2 - Fizz Buzz
# Description: Write a function that receives a StaticArray with integers and returns a new StaticArray object with the
# content from the original array.


from a1_include import *


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    If the number in array is divisible by 3, the corresponding element in the new array = ‘fizz’.
    If the number in is divisible by 5, the corresponding element in the new array = ‘buzz’.
    If the number in is both a multiple of 3 and of 5, the corresponding element in the new array = ‘fizzbuzz’.
    If all other cases, the element in the new array should have the same value as in the original array
    """
    position = 0  # Position in the array.
    length = StaticArray.size(arr)  # Length of the original array.
    new_array = StaticArray(length)  # New Empty Array with the length of the original array.
    while position < StaticArray.size(arr):
        string = ''  # empty string to be used for the corresponding element if change is needed
        index_value = StaticArray.get(arr, position)
        if index_value % 3 == 0:
            string += 'fizz'  # if divisible by 3 then add fizz to the string
            StaticArray.set(new_array, position, string)
        if index_value % 5 == 0:
            string += 'buzz'  # if divisible by 5 then add buzz to the string
            StaticArray.set(new_array, position, string)
        if index_value % 3 != 0 and index_value % 5 != 0:
            StaticArray.set(new_array, position, index_value)  # if neither, then keep value
        position += 1  # Position is move one each time it iterates through the list.
    return new_array


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
