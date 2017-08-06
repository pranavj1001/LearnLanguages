class Node(object):
    
    # constructor
    # here we will create a node and initialize its left and right child with None
    # also balance is used here to balance the AVL tree
    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.leftChild = None
        self.rightChild = None
        self.balance = 0
    
    # method to insert nodes
    def insert(self, data, parentNode):
        
        # if the value of the data to be inserted is less than the current Node then go left
        if data < self.data:
            # if the leftChild is none then create node below it and the currentNode as its parentNode
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            # traverse more
            else:
                self.leftChild.insert(data, parentNode)
        # if the value of the data to be inserted is more than the current Node then go right                
        else:
            # if the rightChild is none then create node below it and the currentNode as its parentNode
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            # traverse more                
            else:
                self.rightChild.insert(data, parentNode)

        return parentNode
    
    # method to traverse in IN-ORDER way i.e. the left child + root node + the right child
    def traverseInorder(self):
        if self.leftChild:
            self.leftChild.traverseInorder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInorder()
    
    # method to get the maximum value
    def getMax(self):
        if not self.rightChild:
            return self.data
        else:
            return self.rightChild.getMax()
    
    # method to get the minimum value
    def getMin(self):
        if not self.rightChild:
            return self.data
        else:
            return  self.leftChild.getMin()
