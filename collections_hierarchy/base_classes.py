from .node import Node


class Sequenceable(object):
    def __init__(self, start = None):
        self.start = start

    def get_elements(self):
        """Returns an array of all Node values in the stack"""
        node = self.start
        values = []

        while node is not None:
            values.append(node.value)
            node = node.next
            
        return values

    def get_end(self):
        """Returns the last element in the stack"""
        lastNode = self.start
        nextNode = self.start
        while nextNode is not None:
            lastNode = nextNode
            nextNode = lastNode.next
        return lastNode
    

class Appendable(object):
    def append(self, element):
        """Adds a node to the end of the stack"""
        last = self.get_end()
        if last is None:
            self.start = Node(element)
        else:
            last.next = Node(element)


class Popable(object):
    def pop(self):
        """Removes the first node from the stack"""
        if self.start is None:
            raise IndexError()
        
        first = self.start
        self.start = first.next
        return first.value;


class Pushable:
    def push(self, element):
        """Inserts a node at the start of the stack"""
        first = Node(element, self.start)
        self.start = first
        
