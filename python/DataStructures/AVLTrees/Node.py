class Node(object):

    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.leftChild = None
        self.rightChild = None
        self.balance = 0

    def insert(self, data, parentNode):

        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)
        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)

        return parentNode

    def traverseInorder(self):
        if self.leftChild:
            self.leftChild.traverseInorder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInorder()

    def getMax(self):
        if not self.rightChild:
            return self.data
        else:
            return self.rightChild.getMax()

    def getMin(self):
        if not self.rightChild:
            return self.data
        else:
            return  self.leftChild.getMin()