class Node(object):

    # constructor
    # here we will create a node and initialize its left and right child with None
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # method to insert nodes
    def insertRecursive(self, data):

        # if the value of the data to be inserted is less than the current Node then go left
        if data < self.data:

            # the current node has no left child
            if not self.leftChild:
                self.leftChild = Node(data)

            # the current node has a left child
            else:
                self.leftChild.insertRecursive(data)

        # if the value of the data to be inserted is more than the current Node then go right
        else:

            # the current node has no right child
            if not self.rightChild:
                self.rightChild = Node(data)

            # the current node has a right child
            else:
                self.rightChild.insertRecursive(data)

    # method to remove a node
    def removeRecursive(self, data, parentNode):

        # if and elif's aim is to reach to the node which is to be removed

        # if the data to be removed is less than the current node then go left
        if data < self.data:
            if self.leftChild:
                self.leftChild.removeRecursive(data, self)

        # if the data to be removed is more than the current node then go right
        elif data > self.data:
            if self.rightChild:
                self.rightChild.removeRecursive(data, self)

        # we reached the node which is to be removed
        else:

            # if the node has 2 children (left and right)
            if self.leftChild and self.rightChild:
                self.data = self.rightChild.getMin()
                self.rightChild.removeRecursive(self.data, self)

            # if the parent node has one left child
            elif parentNode.leftChild == self:

                # if the node to be removed has a left child
                if self.leftChild:
                    tempNode = self.leftChild

                # if the node to be removed has a right child
                else:
                    tempNode = self.rightChild

                parentNode.leftChild = tempNode

            # if the parent node has one right child
            elif parentNode.rightChild == self:

                # if the node to be removed has a left child
                if self.leftChild:
                    tempNode = self.leftChild

                # if the node to be removed has a right child
                else:
                    tempNode = self.rightChild

                parentNode.rightChild = tempNode

    # method to get the minimum value
    def getMin(self):

        if not self.leftChild:
            return self.data
        else:
            return self.leftChild.getMin()

    # method to get the maximum value
    def getMax(self):

        if not self.rightChild:
            return self.data
        else:
            return self.rightChild.getMax()

    # method to traverse in IN-ORDER way i.e. the left child + root node + the right child
    def traverseInOrder(self):

        if self.leftChild:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInOrder()