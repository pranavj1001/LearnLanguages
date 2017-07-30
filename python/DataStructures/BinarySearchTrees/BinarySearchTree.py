from Node import Node

class BinarySearchTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insertRecursive(data)

    def remove(self, dataToRemove):
        if self.rootNode:
            if self.rootNode.data == dataToRemove:
                tempNode = Node(None)
                tempNode.leftChild = self.rootNode;
                self.rootNode.removeRecursive(dataToRemove, tempNode)
            else:
                self.rootNode.removeRecursive(dataToRemove, None)

    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()