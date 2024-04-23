from dataclasses import dataclass

@dataclass
class Node:
    data:object
    left = None
    right = None

    def __repr__(self):
        return str(self.data)

@dataclass
class LinkedList:
    head: Node= None

    def __repr__(self):
        node = self.head
        nodes = []
        nodes.append('None')
        while node is not None:
            nodes.append(node.data)
            node = node.right
        nodes.append('None')
        return '<->'.join(nodes)
    def next(self):
        node = self.head
        if node is None:
            return 'Playlist is empty! or End of Playlist!'
        else:
            nodes = []
            node = node.right
            previous = node.left
            nodes.append(str(previous))

            nodes.append(node.data)
            next = node.right
            nodes.append(str(next))
            return f'Previous Song: {previous} Current Song: {node.data} Next Song: {next}'
    def previous(self):
        node = self.head
        if node is None:
            return 'Playlist is empty! or End of Playlist'
        else:
            nodes = []
            node = node.left
            previous = node.left
            nodes.append(str(previous))
            nodes.append(node.data)
            next = node.right
            nodes.append(str(next))
            return f'Previous Song: {previous} Current Song: {node.data} Next Song: {next}'

playlist = LinkedList()
song1 = Node('Perfect')
song2 = Node('Thinking Out Loud')
song3 = Node('Shape of You')
song4 = Node('Soweto')
song5 = Node('Infinity')
song6 = Node('Rush')

playlist.head = song1
song1.right = song2
song2.right = song3
song3.right = song4
song4.right = song5
song5.right = song6

print(playlist.next())
print(playlist.next())



