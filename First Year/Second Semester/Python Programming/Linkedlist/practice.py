from dataclasses import dataclass

@dataclass
class Node:
    data:object
    next = None

    def __repr__(self):
        return f"Node: {self.data}"

@dataclass
class LinkedList:
    head=None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return f"LinkedList: {'->'.join(nodes)}"

Names = LinkedList()
Michael = Node('Michael')
Names.head = Michael
Agonsi = Node('Agonsi')
Michael.next = Agonsi
Chidera = Node('Chidera')
Agonsi.next = Chidera

print(Names)