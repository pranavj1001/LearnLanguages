from Node import Node

class BinarySearchTree(object):

    # constructor
    # here we initialize the root node
    def __init__(self):
        self.rootNode = None

    # method to insert a node
    def insert(self, data):
        # if we are inserting a node for the first time
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insertRecursive(data)

    # method to remove a node
    def remove(self, dataToRemove):
        # check if the tree is empty or not
        if self.rootNode:
            # if we have to remove the root node
            if self.rootNode.data == dataToRemove:
                # create a new node
                tempNode = Node(None)
                # make its leftChild the rootNode
                tempNode.leftChild = self.rootNode
                # then continue with the remove process
                self.rootNode.removeRecursive(dataToRemove, tempNode)
            else:
                self.rootNode.removeRecursive(dataToRemove, None)

    # method to display the max node of the tree
    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    # method to display the min node of the tree
    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    # method to traverse through the tree
    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()