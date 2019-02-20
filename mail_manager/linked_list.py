
class Node:
    """
    The nodes are the separated objects that will conform the Linked List.
    """

    def __init__(self, data=None):
        """
        Initializes a node instance that will contain some data.

        :param data: content of the node. This could be any object, for example, an email.
        """
        pass

class LinkedList:
    """
    This class implements a linked list.

    A linked list is a linear data structure where each element is a separate object.
    Linked list elements are not stored at contiguous location; the elements are linked using pointers.
    In this case each separated object belongs to the class Node.
    """

    def __init__(self):
        """
        Initializes the linked list. Take into account that you'll need to keep track of the first and/or
        the last element. Maybe is advisable also to have an updated size attribute.
        """
        pass

    def append(self, item):
        """
        Add an item to the end of the list.
        """
        pass

    def insert(self, index, item):
        """
        Insert an item at a given position.

        The first argument is the index of the element before which to insert, so a.insert(0, item) inserts
        at the front of the list and a.insert(len(a), item) is equivalent to a.append(item).

        :param index: index where the item should be stored.
        :param item: object to be stored into the linked list.
        """
        pass

    def remove(self, item):
        """
        Remove from the list the first occurrence of item.

        Raises ValueError if there is no such item.

        :param item: object to be removed from the linked list.
        """
        pass

    def pop(self, index=-1):
        """
        Remove the item at the given position in the list, and return it.
        If no index is specified, a.pop() removes and returns the last item in the list.

        Raises IndexError if list is empty or index is out of range.

        :param index: index where the item should be popped (removed and returned).
        """

        return None

    def clear(self):
        """
        Remove all items from the list.
        """
        pass

    def index(self, item, start=0, end=None):
        """
        Return first index of value.

        Raises a ValueError if there is no such item.

        :param item: object to be stored into the linked list.
        :param start: position from which the search is going to start.
        :param end: position at which the search is going to end.

        """
        return 0

    def __len__(self):
        """
        Returns the actual size, it is, the number of elements stored in the linked list.

        :return: the number of elements currently stored in the linked list.
        """
        return 0

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        return ""

