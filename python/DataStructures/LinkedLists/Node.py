class Node(object):

    # constructor
    # every node will have a data and a reference to the nextNode
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    # method to remove an element
    def removeRecursive(self, data, previousNode):

        #if tra
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode:
                self.nextNode.removeRecursive(data, self)