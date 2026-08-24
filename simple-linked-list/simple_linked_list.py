class EmptyListException(Exception):
    """
    Empty list exception
    """
    
    def __init__(self, message: str):
        self.message = message
        

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        return self.value

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, values: list = None):
        self.head = None
        self.values = values

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield
        

    def __len__(self):
        pass

    def head(self):
        return self.head

    def push(self, value):
        if self.values:
            node = Node(value)
            self.head = node
            node.next = self.head
        
        else:
            node = EmptyListException('The list is empty.')

    def pop(self):
        pass

    def reversed(self):
        pass
