from Node import Node

class TST(object):

    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node, key, value, index):

        character = key[index]

        if node is None:
            node = Node(character)

        if character < node.char:
            node.leftNode = self.putItem(node.leftNode, key, value, index)
        elif character > node.char:
            node.rightNode = self.putItem(node.rightNode, key, value, index)
        elif index < len(key) - 1:
            node.middleNode = self.putItem(node.middleNode, key, value, index + 1)
        else:
            node.value = value

        return node

    def get(self, key):

        node = self.getItem(self.rootNode, key, 0)

        if node is None:
            return None

        return node.value

    def getItem(self, node, key, index):

        if node is None:
            return None

        character = key[index]

        if character < node.char:
            return self.getItem(node.leftNode, key, index)
        elif character > node.char:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index + 1)
        else:
            return node
