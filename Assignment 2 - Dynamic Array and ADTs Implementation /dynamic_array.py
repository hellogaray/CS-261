# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment 2 - Part 1
# Description: Implement a Dynamic Array class by completing provided skeleton code.
# Last revised: 10/21/2020


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)
        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the underlying storage for the array elements. It does not change values or order of
        any elements currently stored in the dynamic array.
        """
        if new_capacity < self.size or new_capacity <= 0:  # No action if negative int or new_capacity < current size.
            return
        new_array = StaticArray(new_capacity)  # Creates a new empty array using the new capacity.
        for i in range(self.size):
            new_array[i] = self.data[i]
        self.data = new_array  # Replaces the current data with new_array.
        self.capacity = new_capacity  # Replaces the capacity data with new_capacity.

    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array. If internal storage is at capacity it doubles it.
        """
        if self.size >= self.capacity:  # If internal storage is already full double its capacity.
            self.resize(self.capacity * 2)
        self.data[self.size] = value  # Inserts the given value at size.
        self.size += 1  # Size increment of one.

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the dynamic array. If internal storage is at capacity it
        doubles it. Raises a Dynamic Array error if index is out of array (index is greater than size or less than 0).
        """
        if self.size < index or index < 0:  # Raises Dynamic Array error if index is greater than size or less than 0.
            raise DynamicArrayException
        if self.size >= self.capacity:  # If internal storage is already full double its capacity.
            self.resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value  # Inserts the given value at index.
        self.size += 1  # Size increment of one.

    def get_at_index(self, index: int) -> object:
        """
        Returns value from the specific index in the dynamic array. Raises a Dynamic Array error if index is out of
        array (index is greater than size or less than 0).
        """
        if self.size <= index or index < 0:  # Raises Dynamic Array error if index is greater than size or less than 0.
            raise DynamicArrayException
        else:
            return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        Removes the element from the dynamic array given its index. Raises a Dynamic Array error if index is out of
        array (index is greater than size or less than 0).
        """
        if self.size <= index or index < 0:  # Raises Dynamic Array error if index is greater than size or less than 0.
            raise DynamicArrayException
        if self.size < (self.capacity / 4) and self.capacity > 10:  # Reduces size if size < 1/4 of the capacity.
            if self.size * 2 > 10:
                self.resize(self.size * 2)
            if self.size * 2 < 10:
                self.resize(10)
        for i in range(index, self.size - 1, 1):  # Replaces positions by iterating through array.
            self.data[i] = self.data[i + 1]
        self.size -= 1  # Size decreased by one.

    def slice(self, start_index: int, quantity: int) -> object:
        """
        Returns a new Dynamic Array object that contains the requested number of elements from the original array
        starting with the element located at the requested start index.
        """
        if start_index < 0 or quantity < 0 or quantity + start_index > self.size or start_index == self.size:
            # Raises error if index is greater than size or less than 0.
            raise DynamicArrayException
        new_array = DynamicArray()  # Creates a new Dynamic Array.
        starting_point = 0  # Start index for new array.
        for i in range(start_index, quantity + start_index):  # Iterates through new array and copies selected values.
            new_array.insert_at_index(starting_point, self.data[i])
            starting_point += 1
        new_array.size = quantity
        return new_array

    def merge(self, second_da: object) -> None:
        """
        Takes another Dynamic Array object as a parameter and appends all elements from the second array to the
        current one in the same order as they are stored in the second array.
        """
        for i in range(0, second_da.size):
            self.append(second_da.get_at_index(i))

    def map(self, map_func) -> object:
        """
        Creates a new Dynamic Array where the value of each element is derived by applying a given map_func to the
        corresponding value from the original array.
        """
        new_array = DynamicArray()  # Creates a new Dynamic Array.
        for i in range(0, self.size):  # Iterates through new array and sets new values based on function.
            new_array.append(map_func(self.get_at_index(i)))
        return new_array

    def filter(self, filter_func) -> object:
        """
        Creates a new Dynamic Array populated only with those elements from the
        original array for which filter_func returns True.
        """
        new_array = DynamicArray()  # Creates a new Dynamic Array.
        for i in range(0, self.size):  # Iterates through new array and returns only when filter_func returns True.
            if filter_func(self.get_at_index(i)):  # If statement returns true then proceed with code below.
                new_array.append(self.get_at_index(i))
        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies the reduce_func to all elements of the Dynamic Array and returns the resulting value.
        Takes an optional initializer parameter. If this parameters is not provided, first value in hte array is used.
        """
        if initializer is None:  # Scenarios were initializer is None.
            if self.size < 1:  # If there are no values, do nothing.
                return
            if self.size == 1:  # If there's only one value, return value.
                return self.get_at_index(0)
            else:
                stored_item = reduce_func(self.get_at_index(0), self.get_at_index(1))
                for i in range(2, self.size):
                    func_result = reduce_func(stored_item, self.get_at_index(i))
                    stored_item = func_result
                return stored_item
        else:  # Scenarios were initializer is not None.
            if self.size < 1:  # If there are no values, return initializer.
                return initializer
            if self.size == 1:  # If there's only one value, use value and initializer.
                return reduce_func(initializer, self.get_at_index(0))
            else:
                stored_item = reduce_func(initializer, self.get_at_index(0))
                for i in range(1, self.size):
                    func_result = reduce_func(stored_item, self.get_at_index(i))
                    stored_item = func_result
                return stored_item




# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    # remove_at_index - example 2
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
