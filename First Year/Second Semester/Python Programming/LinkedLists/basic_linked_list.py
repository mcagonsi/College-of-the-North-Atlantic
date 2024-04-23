from dataclasses import dataclass


@dataclass
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f'Node: {self.data}'

    def __str__(self):
        return f'Node: This is string method {self.data}'

test1 = Node(2)

@dataclass
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.nextNode
        nodes.append('None')
        return '->'.join(nodes)

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertAtTail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.nextNode:
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode

    def insertAtPosition(self, data, position):
        newNode = Node(data)
        currentNode = self.head
        pos = 0

        if pos == position:
            self.insertAtHead(newNode)
        else:
            while (currentNode != None and (pos+1) != position):
                pos = pos + 1
                currentNode = currentNode.nextNode

            if currentNode != None:
                newNode.nextNode = currentNode.nextNode
                currentNode.nextNode = newNode
            else:
                print('Position does not exist')


llist = LinkedList()
# print(llist)

firstNode = Node('a')
llist.head = firstNode

secondNode = Node('b')
thirdNode = Node('c')

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

llist.insertAtHead(0)
llist.insertAtTail(100)
llist.insertAtPosition(50, 2)

print(llist)