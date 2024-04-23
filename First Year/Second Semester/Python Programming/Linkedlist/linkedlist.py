from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node:{self.data}'


class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return '->'.join(nodes)

    def insertAtHead(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            self.head = new_node
            new_node.next = current_node
    def insertAtTail(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insertAtPosition(self,position,data):
        new_node = Node(data)
        current_node = self.head
        pos = 0
        if pos == position:
            self.insertAtHead(new_node)
        else:

            while (current_node != None and (pos + 1) != position):
                pos = pos + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print('Position does not exist')



llist = Linkedlist()
test1 = Node('a')
llist.head = test1
test2 = Node('b')
test1.next = test2
test3 = Node('Michael')
test2.next = test3
llist.insertAtHead('4')
llist.insertAtTail('Dinn')
llist.insertAtPosition(2,'Agonsi')

print(llist)
