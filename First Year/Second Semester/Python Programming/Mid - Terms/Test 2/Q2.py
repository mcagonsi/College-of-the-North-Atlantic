from dataclasses import dataclass
@dataclass
class Node:
    data:object
    next = None

    def __repr__(self):
        return f'{self.data}'
class LinkedList:
    head:None

    def insert(self,data):
        node = self.head
        if node == None:


