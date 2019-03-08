class Node:
    """
    The nodes are the separated objects that will conform the Linked List.
    """

    def __init__(self, data=None):
        """
        Initializes a node instance that will contain some data.

        :param data: content of the node. This could be any object, for example, an email.
        """

        self.next = None
        self.data = data


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
        self.size = 0
        self.first = None
        self.last = None

    def append(self, item):
        """
        Add an item to the end of the list.
        """
        node = Node(item)

        if not self.size:
            self.first = node
        else:
            self.last.next = node

        self.last = node
        self.size += 1

    def insert(self, index, item):
        """
        Insert an item at a given position.

        The first argument is the index of the element before which to insert, so a.insert(0, item) inserts
        at the front of the list and a.insert(len(a), item) is equivalent to a.append(item).

        :param index: index where the item should be stored.
        :param item: object to be stored into the linked list.
        """
        if index > self.size or index < 0:
            raise IndexError("Index is out of range")

        if index == self.size:
            self.append(item)
        else:

            previous = None
            node = Node(item)
            current = self.first
            iter = 0
            while current is not None and index != iter:
                previous = current
                current = current.next
                iter += 1

            if current == self.first:
                node.next = self.first
                self.first = node
            elif index == iter:
                previous.next = node
                node.next = current
            elif current == self.last:
                current.next = node
                self.last = node
            self.size += 1

    def remove(self, item):
        """
        Remove from the list the first occurrence of item.

        Raises ValueError if there is no such item.

        :param item: object to be removed from the linked list.
        """

        if not self.size:
            raise IndexError("The list is empty")

        current = self.first

        if self.size == 1:
            self.first = None
            self.last = None

        else:
            previous = None
            iter = 0

            while current.next is not None and current.data != item:
                previous = current
                current = current.next
                iter += 1

            if current.data == item:
                if current == self.first:
                    self.first = current.next
                else:
                    previous.next = current.next
                    if current == self.last:
                        self.last = previous
                self.size -= 1
            else:
                raise ValueError("There is no such item")

        return current.data

    def pop(self, index=-1):
        """
        Remove the item at the given position in the list, and return it.
        If no index is specified, a.pop() removes and returns the last item in the list.

        Raises IndexError if list is empty or index is out of range.

        :param index: index where the item should be popped (removed and returned).
        """

        if not self.size:
            raise IndexError("The list is empty")
        if index >= self.size:
            raise IndexError("Index is out of range")
        if index == -1:
            index = self.size - 1

        previous = None
        current = self.first

        if self.size == 1:
            self.first = None
            self.last = None

        else:
            iter = 0

            while current.next is not None and index != iter:
                previous = current
                current = current.next
                iter += 1

            if current == self.first:
                self.first = current.next
            else:
                previous.next = current.next
                if current == self.last:
                    self.last = previous

        return current.data

    def clear(self):
        """
        Remove all items from the list.
        """
        self.size = 0
        self.first = None
        self.last = None

    def index(self, item, start=0, end=None):
        """
        Return first index of value.

        Raises a ValueError if there is no such item.

        :param item: object to be searched in the linked list.
        :param start: position from which the search is going to start.
        :param end: position at which the search is going to end.

        """
        end = self.size-1 if end is None else end
        node = Node(item)
        i = 0
        current = self.first
        while i != start:
            current = current.next
            i += 1
        while current.data is not node.data and i != end:
            current = current.next
            i += 1
        if i == end:
            if current.data == node.data:
                return str(i)
            else:
                raise ValueError("There is no such item")
        return str(i)

    def __len__(self):
        """
        Returns the actual size, it is, the number of elements stored in the linked list.

        :return: the number of elements currently stored in the linked list.
        """
        return self.size

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        str_aux = ""

        current = self.first
        while current is not None:

            str_aux = str_aux + ", " + str(current.data)

            current = current.next
        str_aux = "[" + str_aux[2:] + "]"
        return str_aux
