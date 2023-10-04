# Course: CS261 - Data Structures
# Assignment: 5
# Student: Leonel Garay
# Description: Implement the HashMap class by completing provided skeleton code.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash

class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def empty_buckets(self) -> int:
        """
        Returns a number of empty buckets in the hash table.
        """
        counter = 0  # Keeps track of how many emtpy buckets are found.
        for i in range(0, self.capacity):
            if self.buckets.get_at_index(i).length() == 0:  # If the bucket is empty add 1 to counter variable.
                counter += 1
        return counter

    def table_load(self) -> float:
        """
        Returns the current hash table load factor.
        """
        return self.size / self.capacity

    def clear(self) -> None:
        """
        Clears the content of the hash map. It does not change underlying hash table capacity.
        """
        for i in range(0, self.capacity):  # Replaces each value within range for an emtpy LinkedList.
            self.buckets.set_at_index(i, LinkedList())
        self.size = 0  # Sets the size of the map back to 0.

    def put(self, key: str, value: object) -> None:
        """
        Updates the key / value pair in the hash map. If a given key already exists in the hast map, its
        associated value should be replaced with the new value.
        """
        position = self.buckets.get_at_index(self.hash_function(key) % self.capacity)  # Gets the value at index.
        if position.contains(key) is not None:  # If the given key is already in the hash map, replace with new value.
            position.remove(key)  # Removes the key on the table.
            position.insert(key, value)  # Add the key with the new value.
        else:  # If the given key is not found, then insert the new key and value and increase size by one.
            position.insert(key, value)
            self.size += 1

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map; otherwise, it returns False.
        """
        position = self.buckets.get_at_index(self.hash_function(key) % self.capacity)  # Gets the value at index.
        if position.contains(key) is None:  # If contains return None, key wasn't found, return False.
            return False
        else:  # Else it was found, return true.
            return True

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key. If the key is not in the hash map, the method returns None.
        """
        position = self.buckets.get_at_index(self.hash_function(key) % self.capacity)  # Gets the value at index.
        if self.contains_key(key) is True:  # If contains_key returns True, return the value of that key.
            return position.contains(key).value
        else:  # Else it wasn't found, return None.
            return None

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the hash map.
        If a given key is not in the map it does nothing.
        """
        position = self.buckets.get_at_index(self.hash_function(key) % self.capacity)  # Gets the value at index.
        if position.contains(key) is not None:  # If the given key is  in the hash map remove it and reduce size by 1.
            position.remove(key)  # Removes the key on the table.
            self.size -= 1  # Reduces size by one.
        else:  # If given key is not in the map it does nothing.
            return

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table.
        """
        new_dynamic_array, new_linked_list = DynamicArray(), LinkedList()   # New Dynamic Array and Linked List.
        if new_capacity < 1:  # If new_capacity is less than 1, do nothing.
            return
        else:
            for i in range(new_capacity):  # Sets the new capacity n amount of times based on new_capacity.
                new_dynamic_array.append(LinkedList())
            for i in range(0, self.capacity):
                for j in self.buckets.get_at_index(i):  # Gets the nodes and inserts them on Linked List.
                    new_linked_list.insert(j.key, j.value)
            self.size, self.capacity, self.buckets = 0, new_capacity, new_dynamic_array  # Sets new values for fields.
            for node in new_linked_list:  # Places the nodes on the dynamic array.
                self.put(node.key, node.value)

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all keys stores in your hash map.
        """
        dynamic_array = DynamicArray()  # Creates a new Dynamic Array to be used for keys.
        for i in range(0, self.buckets.length()):  # Iterates through the items on the table.
            for j in self.buckets.get_at_index(i):  # Gets the key.
                dynamic_array.append(j.key)  # Appends key to the new dynamic array.
        return dynamic_array


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)
