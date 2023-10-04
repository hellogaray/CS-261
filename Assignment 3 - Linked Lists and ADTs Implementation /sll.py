# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: Assignment #3 - Part 1
# Description: Implement a Deque and B ag ADT interfaces with a Singly Linked List data structure.


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel).
        """
        temporary_node = SLNode(value)  # Temporary node to store the value.
        temporary_node.next = self.head.next  # Sets node.next to the what is currently head.next.
        self.head.next = temporary_node  # Updates head.next to the temporary value.
        return

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (right before the back sentinel).
        """
        current = self.head  # Uses current to traverse the list to find last node.
        temporary_node = SLNode(value)  # Temporary node to store the value.
        temporary_node.next = self.tail  # Sets node.next to the tail.
        while current.next != self.tail:
            current = current.next
        current.next = temporary_node
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list.
        """
        temporary_node = self.head  # Uses current to traverse the list to find last node.
        if index < 0 or index > self.length():  # If index is out of range raise exception.
            raise SLLException()
        while index > 0:
            """
            Subtracts 1 out of index until index is 0, this will make it that it traverses through the list until its 
            at 0 meaning it can now place the value in the current node. 
            """
            temporary_node = temporary_node.next  # Temporary node value will be replaced with the next value.
            index -= 1  # Subtracts 1 out of the index.
        placement_value = SLNode(value)  # Uses the variable to save the newly created node.
        placement_value.next = temporary_node.next  # Places the node to use the next value of temporary node.
        temporary_node.next = placement_value  # Replaces the value saved in temporary node with the new node.

    def remove_front(self) -> None:
        """
        Removes the first node from the list.
        """
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise SLLException()
        else:
            self.head.next = self.head.next.next  # Replaces head.next with whatever is after head.next.

    def remove_back(self) -> None:
        """
        Removes the last node from the list.
        """
        current = self.length()  # Sets current to the length of the list.
        to_remove_node = self.head  # Sets the node to remove to the head.
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise SLLException()
        while current > 1:
            to_remove_node = to_remove_node.next  # Replaces variable with the next value in the list.
            current -= 1  # Subtracts 1 out of index until index while is greater than 0
        to_remove_node.next = self.tail

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node from the list given its index.
        """
        to_remove_node = self.head  # Sets the node to remove to the head.
        if index < 0 or index > self.length() - 1:  # If index is out of range raise exception.
            raise SLLException()
        while index > 0:
            to_remove_node = to_remove_node.next  # Replaces variable with the next value in the list.
            index -= 1  # Subtracts 1 out of index until index while is greater than 0.
        to_remove_node.next = to_remove_node.next.next  # Replaces to_remove_node.next with the next one.

    def get_front(self) -> object:
        """
        Returns value from the first node in the list without remove it.
        """
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise SLLException()
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        Returns value from the last node in the list without remove it.
        """
        current = self.length()  # Sets current to the length of the list.
        last_value = self.head  # Sets the node to return to the head.
        if self.is_empty():  # If the list is empty, the method raises an exception.
            raise SLLException()
        while current > 0:
            last_value = last_value.next  # Replaces variable with the next value in the list.
            current -= 1  # Subtracts 1 out of current until index while is greater than 0.
        return last_value.value

    def remove(self, value: object) -> bool:
        """
        Traverses the list from beginning to the end and removes the first node in the list that matches the provided
        value object. Returns True if some node was actually removed from the list. Otherwise it returns False.
        """
        position = self.length()  # Sets current to the length of the list.
        current = self.head.next  # Sets the node to return to node next to head.
        while position > 0:  # Iterates through the list as long as position is greater than 0.
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
        current = self.head.next  # Sets the node to return to node next to head.
        while position > 0:  # Iterates through the list as long as position is greater than 0.
            if current.value == value:
                current = current.next  # Sets current to the next value.
                counter += 1  # Add 1 to counter.
                position -= 1  # Subtracts 1 out of current until index while is greater than 0.
            else:  # If no matching value it continues to iterate.
                current = current.next  # Sets current to the next value.
                position -= 1  # Subtracts 1 out of current until index while is greater than 0.
        return counter

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList object that contains the requested number of nodes from the original list
        starting with the node located at the requested start index.
        """
        new_list = LinkedList()  # Creates a new list.
        start_node = self.head.next  # Sets the start
        nl_start_node = new_list.head  # Sets current to the new list head.
        if start_index == 0 and size == 0 and self.length() > 0:
            return new_list
        if start_index < 0 or start_index > self.length() or start_index + size > self.length() or size > self.length()\
                or size < 0 or start_index == self.length() and size == 0 or self.length() == 0:
            raise SLLException()
        while start_index > 0:  # Finds the starting value for the new list. 
            start_node = start_node.next
            start_index -= 1
        while size > 0:  # Starts placing the new values on new list until size is 0.
            temporary_node = SLNode(start_node.value)  # Temporary node to store the value.
            temporary_node.next = new_list.tail  # Sets node.next to the tail.
            while nl_start_node.next != new_list.tail:
                nl_start_node = nl_start_node.next
            nl_start_node.next = temporary_node
            start_node = start_node.next  # Sets start node to the next value.
            size -= 1
        return new_list


if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    #
    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)
    #
    #
    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
    #
    #
    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)
    #
    #
    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    #
    # print('\n# get_back example 1')
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
    #
    #
    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)
    #
    #
    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    # print('\n# slice example 2')
    # list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")
