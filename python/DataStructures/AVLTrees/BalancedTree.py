from . import Node

class BalancedTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):

        parentNode = self.rootNode

        if not self.rootNode:
            parentNode = Node(data, None)
            self.rootNode = parentNode
        else:
            parentNode = self.rootNode.insert(data, self.rootNode)

        self.reBalanceTree(parentNode)

    def reBalanceTree(self, parentNode):

        self.setBalance(parentNode)


    def setBalance(self, node):
        node.balance = (self.height(node.rightChild) - self.height(node.leftChild))


    def height(self, node):
        if not node:
            return -1
        else:
            return 1 + max(self.height(node.leftChild), self.height(node.rightChild))