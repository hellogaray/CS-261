# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 1 - Problem 4 - Rotate
# Description: Function that receives two parameters - a StaticArray and an integer value (called steps ). The function
# will create and return a new StaticArray where all elements are from the original array but their position has shifted
# right or left steps number of times. Original array should not be modified.


from a1_include import *


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Rotates the list right or left depending on the parameter (negative or positive). If length is 1 or steps are equal
    to 0 then returns a copy of the original array.
    """
    length = StaticArray.size(arr)  # Length of the original array.
    pos_step_counter = 0  # Sets step_counter to 0.
    neg_step_counter = length  # Sets step_counter to length of array.
    new_array = StaticArray(length)  # Creates a new array so that the original hasn't been altered.
    """ If steps is more than 0 (positive number) then move everything to the right."""
    if steps > 0 and length > 1:
        while pos_step_counter < steps % length:
            position = 0  # Position in the array.
            new_array = StaticArray(length)  # Creates a new array so that the original hasn't been altered.
            pos_step_counter += 1  # Counts the number of steps that have been taken, every runs adds 1.
            last_value = StaticArray.get(arr, length - 1)  # Saves the last value.
            while position < StaticArray.size(arr):
                current_value = StaticArray.get(arr, position)  # Saves the current value based on position.
                if position < length - 1:
                    StaticArray.set(new_array, 0, last_value)  # Sets the last value as the first one.
                    StaticArray.set(new_array, position + 1, current_value)  # Uses the saved value to place next.
                position += 1  # Position is move one each time it iterates through the list.
            arr = new_array  # replaces arr variable with new_array so that the next run uses the new variable.
    """ If steps is less than 0 (negative number) then move everything to the left."""
    if steps < 0 and length > 1:
        while neg_step_counter > steps % length:
            position = length - 1  # Position in the array.
            new_array = StaticArray(length)  # Creates a new array so that the original hasn't been altered.
            neg_step_counter -= 1  # Counts the number of steps that have been taken, every runs subtracts 1.
            first_value = StaticArray.get(arr, 0)  # Saves the first value.
            while position > 0:
                current_value = StaticArray.get(arr, position)  # Saves the current value based on position.
                second_value = StaticArray.get(arr, 1)  # Saves the second value in the list arr[1].
                if position > 0:
                    StaticArray.set(new_array, length - 1, first_value)  # Sets the last value as the first one.
                    StaticArray.set(new_array, position - 1, current_value)  # Uses the saved value to place before.
                position -= 1  # Position is move one each time it iterates through the list.
            arr = new_array  # replaces arr variable with new_array so that the next run uses the new variable.
    """ If steps is empty or 0 then just return new_array equal to the original array."""
    if steps == 0 or steps % length == 0 or length == 1:
        new_array = arr
    return new_array


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [-95424, -62173]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)
