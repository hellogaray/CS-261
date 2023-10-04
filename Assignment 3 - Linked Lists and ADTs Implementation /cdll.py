# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment #3 - Part 3
# Description: Deque and Bag ADT interfaces with a circular doubly linked list data structure.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel).
        """
        temporary_node = DLNode(value)  # Creates a "temporary" node to be used.
        temporary_node.next = self.sentinel.next  # Sets the next of temporary_node.
        temporary_node.prev = self.sentinel  # Sets the prev of temporary_node.
        temporary_node.next.prev = temporary_node  # Updates the previous of the next node after temporary node.
        self.sentinel.next = temporary_node  # Updates the sentinel.next.

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (right before the back sentinel).
        """
        temporary_node = DLNode(value)  # Creates a "temporary" node to be used.
        temporary_node.next = self.sentinel  # Sets the next of temporary_node.
        temporary_node.prev = self.sentinel.prev  # Sets the prev of temporary_node.
        temporary_node.prev.next = temporary_node  # Updates the next of the previous node after temporary node.
        self.sentinel.prev = temporary_node  # Updates the sentinel.prev.

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list.
        """
        temporary_node = self.sentinel  # Uses current to traverse the list to find last node.
        if index < 0 or index > self.length():  # If index is out of range raise exception.
            raise CDLLException()
        while index > 0:
            """
            Subtracts 1 out of index until index is 0, this will make it that it traverses through the list until its 
            at 0 meaning it can now place the value in the current node. 
            """
            temporary_node = temporary_node.next  # Temporary node value will be replaced with the next value.
            index -= 1  # Subtracts 1 out of the index.
        placement_value = DLNode(value)  # Uses the variable to save the newly created node.
        placement_value.next = temporary_node.next  # Places the node to use the next value of temporary node.
        placement_value.prev = temporary_node  # Updates prev value of placement_value to the temporary node.
        placement_value.next.prev = placement_value  # Updates the prev value of the next value after placement value.
        temporary_node.next = placement_value  # Updates next value of temporary node to the placement value.

    def remove_front(self) -> None:
        """
        Removes the first node from the list.
        """
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise CDLLException()
        else:
            self.sentinel.next.next.prev = self.sentinel  # Replaces prev for whatever is after the front node.
            self.sentinel.next = self.sentinel.next.next  # Replaces sentinel.next with whatever is after sentinel.next.

    def remove_back(self) -> None:
        """
        Removes the back node from the list.
        """
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise CDLLException()
        self.sentinel.prev.prev.next = self.sentinel  # Replaces next of whatever is after sentinel.prev with sentinel.
        self.sentinel.prev = self.sentinel.prev.prev  # Replaces sentinel.prev with whatever is before sentinel.prev.

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index.
        """
        to_remove_node = self.sentinel  # Sets the node to remove to the head.
        if index < 0 or index > self.length() - 1:  # If index is out of range raise exception.
            raise CDLLException()
        while index > 0:
            to_remove_node = to_remove_node.next  # Replaces variable with the next value in the list.
            index -= 1  # Subtracts 1 out of index until index while is greater than 0.
        to_remove_node.next.next.prev = to_remove_node  # Replaces prev of next.next with var.
        to_remove_node.next = to_remove_node.next.next  # Replaces next to var with next.next.

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without remove it.
        """
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise CDLLException()
        else:
            return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Returns value from the last node in the list without remove it.
        """
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise CDLLException()
        else:
            return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Traverses the list from beginning to the end and removes the first node in the list that matches the provided
        value object. Returns True if some node was actually removed from the list. Otherwise it returns False.
        """
        position = self.length()  # Sets current to the length of the list.
        current = self.sentinel.next  # Sets the node to return to node next to head.
        while position >= 0:  # Iterates through the list as long as position is greater than 0.
            if current.value == value:  # If it finds a matching value, it removes it and returns True.
                self.remove_at_index(self.length() - position)
                return True
            else:  # If no matching value it continues to iterate.
                current = current.next  # Sets current to the next value.
                position -= 1  # Subtracts 1 out of current until index while is greater than 0.
        return False  # If out of while loop, no value found - return False.

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided value.
        """
        counter = 0  # Sets the counter to 0. This is the value that will be returned.
        position = self.length()  # Sets current to the length of the list.
        current = self.sentinel.next  # Sets the node to return to node next to head.
        while position > 0:  # Iterates through the list as long as position is greater than 0.
            if current.value == value:
                current = current.next  # Sets current to the next value.
                counter += 1  # Add 1 to counter.
                position -= 1  # Subtracts 1 out of current until index while is greater than 0.
            else:  # If no matching value it continues to iterate.
                current = current.next  # Sets current to the next value.
                position -= 1  # Subtracts 1 out of current until index while is greater than 0.
        return counter

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps two nodes given their indices.
        """
        temporary_node1 = self.sentinel.next  # Sets temporary_node1 to the first element.
        temporary_node2 = self.sentinel.next  # Sets temporary_node2 to the first element.
        if index1 < 0 or index1 > self.length() - 1 or index2 < 0 or index2 > self.length() - 1:
            raise CDLLException()  # Raises an Exception when index1 or index2 are out of range.
        if index1 == index2:  # Case when index1 and index2 are the same, do nothing.
            return
        while index1 > 0:  # Iterates through the list until it finds the node at index1.
            temporary_node1 = temporary_node1.next
            index1 -= 1  # Subtracts 1 out of index1 until it gets to 0.
        while index2 > 0:  # Iterates through the list until it finds the node at index2.
            temporary_node2 = temporary_node2.next
            index2 -= 1  # Subtracts 1 out of index2 until it gets to 0.
        if temporary_node1.next == temporary_node2:  # Case when temporary_node1 is next to temporary_node2.
            """ Swap places of temporary_node1 and temporary_node2. """
            temporary_node1.next = temporary_node2.next
            temporary_node2.prev = temporary_node1.prev
            temporary_node2.next = temporary_node1
            temporary_node1.prev = temporary_node2
            temporary_node2.prev.next = temporary_node2
            temporary_node1.next.prev = temporary_node1
        elif temporary_node2.next == temporary_node1:  # Case when temporary_node2 is next to temporary_node1.
            """ Swap places of temporary_node2 and temporary_node1. """
            temporary_node2.next = temporary_node1.next
            temporary_node1.prev = temporary_node2.prev
            temporary_node1.next = temporary_node2
            temporary_node2.prev = temporary_node1
            temporary_node1.prev.next = temporary_node1
            temporary_node2.next.prev = temporary_node2
        else:  # Any other case were indexes are not adjacent.
            """ Remove both temporary_node1 and temporary_node2. """
            temporary_node1.prev.next = temporary_node1.next
            temporary_node1.next.prev = temporary_node1.prev
            temporary_node1.next = temporary_node1.prev
            temporary_node2.prev.next = temporary_node2.next
            temporary_node2.next.prev = temporary_node2.prev
            temporary_node2.next = temporary_node2.prev
            """ Updates temporary_node1 and temporary_node2 prev and next. """
            temporary_node1.prev = temporary_node2.next
            temporary_node2.prev = temporary_node1.next
            temporary_node1.next = temporary_node1.prev
            temporary_node2.next = temporary_node2.prev
            """ Replaces temporary_node2 with temporary_node1 and temporary_node1 with temporary_node2. """
            temporary_node1.next = temporary_node1.next.next
            temporary_node1.next.prev = temporary_node1
            temporary_node1.prev.next = temporary_node1
            temporary_node2.next = temporary_node2.next.next
            temporary_node2.next.prev = temporary_node2
            temporary_node2.prev.next = temporary_node2

    def reverse(self) -> None:
        """
        Reverse the order of the nodes in the list. Reversal is done in place without creating any copies.
        """
        start_position = 0  # Set start_position to 0, this would be the first node in the list.
        end_position = self.length() - 1  # Sets end_position to index of last node.
        if self.length() < 2:  # If the list is less than 2 nodes, simply return.
            return
        if self.length() % 2 == 0:  # If there's an even amount of nodes.
            while start_position != self.length() / 2:
                self.swap_pairs(start_position, end_position)  # Swap the two nodes depending on the positions.
                start_position += 1  # Adds 1 to start position.
                end_position -= 1  # Subtracts 1 out of end position.
        else:  # If there's an uneven amount of nodes.
            while start_position != end_position:
                self.swap_pairs(start_position, end_position)  # Swap the two nodes depending on the positions.
                start_position += 1  # Adds 1 to start position.
                end_position -= 1  # Subtracts 1 out of end position.

    def sort(self) -> None:
        """
        Sorts the content of the list in non-descending order. The sorting is done in place without creating any copies.
        """
        if self.length() < 2:  # If the list is less than 2 nodes, simply return.
            return
        end_index = self.length() - 1  # Sets end_index to the length - 1.
        while end_index > 0:
            temporary_node1 = self.sentinel.next  # Sets temporary_node1 to the following node after the sentinel.
            temporary_node2 = temporary_node1.next  # Sets temporary_node2 to the following node after temporary_node1.
            start_index = 0  # Sets start_index to 0.
            while start_index < end_index:  # Swaps the nodes if node2 is less than node1.
                if temporary_node2.value < temporary_node1.value:  # Swaps the nodes if node2 is less than node1.
                    temporary_node1.next = temporary_node2.next
                    temporary_node2.prev = temporary_node1.prev
                    temporary_node2.next = temporary_node1
                    temporary_node1.prev = temporary_node2
                    temporary_node1.next.prev = temporary_node1
                    temporary_node2.prev.next = temporary_node2
                    temporary_node2 = temporary_node1.next  # Updates temporary_node2 to next node.
                    start_index += 1  # Adds 1 to start index.
                else:  # Only updates variables and moves to next comparison.
                    start_index += 1  # Adds 1 to start index.
                    temporary_node1 = temporary_node2  # Updates temporary_node1 to temporary_node2.
                    temporary_node2 = temporary_node1.next  # Updates temporary_node2 to next node.
            end_index -= 1  # Subtracts 1 out of end index.

    def rotate(self, steps: int) -> None:
        """
        Rotates the linked list by shifting positions of its elements right or left number of times.
        """
        if self.length() < 2:  # If the list is less than 2 nodes or steps is 0, simply return.
            return
        neg_counter = (steps * -1) % self.length()
        pos_counter = steps % self.length()
        if neg_counter == 0 or pos_counter == 0:
            return
        if steps < 0:
            while neg_counter > 0:
                saved_value = self.sentinel.next
                self.sentinel.next = self.sentinel.next.next  # Replaces sentinel.next with what is after sentinel.next.
                saved_value.next = self.sentinel  # Sets the next of saved_value.
                saved_value.prev = self.sentinel.prev  # Sets the prev of saved_value.
                saved_value.prev.next = saved_value  # Updates the next of the previous node after saved_value.
                self.sentinel.prev = saved_value  # Updates the sentinel.prev.
                neg_counter -= 1
        else:
            while pos_counter > 0:
                saved_value = self.sentinel.prev
                self.sentinel.prev.prev.next = self.sentinel  # Replaces next of what is after sentinel.prev w/sentinel.
                self.sentinel.prev = self.sentinel.prev.prev  # Replaces sentinel.prev w/what is before sentinel.prev.
                saved_value.prev = self.sentinel  # Sets the prev of temporary_node.
                saved_value.next = self.sentinel.next  # Sets the next of temporary_node.
                self.sentinel.next = saved_value  # Updates the sentinel.next.
                saved_value.next.prev = saved_value  # Updates the previous of the next node after saved_value.
                pos_counter -= 1

    def remove_duplicates(self) -> None:
        """
        Deletes all nodes that have duplicate values from a sorted linked list. Leaving only nodes with distinct values.
        """
        counter = 0
        temporary_node = self.sentinel.next
        if self.length() < 2:
            return
        rotations = self.length()
        while rotations > 0:
            index = 0
            if self.count(temporary_node.value) > 1:
                num_to_delete = self.count(temporary_node.value)
                while num_to_delete != 0:
                    self.remove(temporary_node.value)
                    num_to_delete -= 1
                    counter = 0
            if self.count(temporary_node.value) == 1:
                counter += 1
            while index >= 0:
                temporary_node = temporary_node.next
                index -= 1
            rotations -= 1


    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':
    # pass
    #
    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)
    #
    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)
    #
    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)
    #
    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)
    #
    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())
    #
    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 5, 4, 3, 6, 7, 8, 9, 10])
    # test_cases = ((0, 1), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# reverse example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5, 6],
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)
    #
    # print('\n# reverse example 2')
    # lst = CircularList(["A", "B", "C", "D"])
    # print(lst)
    # lst.reverse()
    # print(lst)
    #
    #
    # print('\n# reverse example 3')
    #
    #
    # class Student:
    #     def __init__(self, name, age):
    #         self.name, self.age = name, age
    #
    #     def __eq__(self, other):
    #         return self.age == other.age
    #
    #     def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)
    #
    #
    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)
    #
    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)
    #
    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)
    #
    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)
    #
    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    #     [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    #     [0, 1, 1, 2, 3, 3, 4, 5, 5, 6], list("abccd"), list("005BCDDEEFI")
    # )
    #
    # print(list("032hfsha"))
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)
    lst = CircularList([-94366, -80840, -80840, -80840, -77224, -48897, -48897, -42677, -1003, 32203, 32203, 47291, 50935, 50935, 87050, 99704])
    print(lst)
    lst.remove_duplicates()
    print('OUTPUT:', lst)
    lst = CircularList([0, 1, 1, 2, 3, 3, 4, 5, 5, 6])
    print(lst)
    lst.remove_duplicates()
    print('OUTPUT:', lst)
    # print('\n# odd_even example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], list('ABCDE'),
    #     [], [100], [100, 200], [100, 200, 300],
    #     [100, 200, 300, 400],
    #     [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E'])
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)
