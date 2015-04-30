import sys

class node:
    def __init__(self):
        self.data = None
        self.previous = None
        self.next = None
        
    def __str__(self):
        return self
        
    def remove(self):
        self.next.previous = self.previous
        self.previous.next = self.next
    


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        return self
        
    def AddNode(self, data):
        n = node()
        n.data = data
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next

    def AddNodeFirst(self,data):
        n = node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n
