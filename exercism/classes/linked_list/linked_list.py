class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.length = 0

    def push(self, new_value: int):
        """
        Insert value at the back (the end) of the list.
        """
        new_node = Node(new_value, succeeding=self.first, previous=self.last)

        if self.length == 0:
            self.first = self.last = new_node
            self.last.previous = new_node
            self.last.succeeding = new_node
            self.first.previous = new_node
            self.first.succeeding = new_node
        elif self.length == 1:
            self.last.previous = new_node
            self.last.succeeding = new_node
            self.last = new_node
        else:
            self.last.succeeding = new_node
            self.first.previous = new_node
            self.last = new_node

        self.length += 1

    def pop(self) -> int:
        """
        Return and remove the last value of the list.
        """
        last_node_value = self.last.value

        if self.length == 1:
            self.first = self.last = None
        else:
            self.first.succeeding = self.first
            self.first.previous = self.first
            self.last = self.first

        self.length -= 1

        return last_node_value

    def shift(self) -> int:
        """
        Return and remove the first value of the list.
        """
        first_node_value = self.first.value

        if self.length == 1:
            self.first = self.last = None
        else:
           self.first.succeeding.previous = self.last
           self.last.succeeding = self.first.succeeding 
           self.first = self.first.succeeding

        self.length -= 1

        return first_node_value

    def unshift(self, new_value: int):
        """
        Insert value at the front (the beginning) of the list.
        """
        new_node = Node(value=new_value, succeeding=self.first, previous=self.last)

        if self.is_empty():
            self.first = self.last = new_node
            self.last.previous = new_node
            self.last.succeeding = new_node
            self.first.previous = new_node
            self.first.succeeding = new_node
        elif self.length == 1:
            self.first.previous = new_node
            self.first.succeeding = new_node
            self.last = self.first
            self.first = new_node
        else:
            self.last.succeeding = new_node
            self.first.previous = new_node
            self.first = new_node

        self.length += 1

    def is_empty(self) -> bool:
        """
        Return whether the list has node nodes, i.e. its length is
        equals to 0.
        """
        return self.length == 0

