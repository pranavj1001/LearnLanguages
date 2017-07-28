class Node(object):

    # constructor
    # every node will have a data and a reference to the nextNode
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    # O(n)   method to support the remove method from LinkedList.py
    def removeRecursive(self, data, previousNode):

        # if node we want to delete is reached
        if self.data == data:
            # link previous node to the nextnode
            previousNode.nextNode = self.nextNode

            # delete stuff i.e. free garbage values
            del self.data
            del self.nextNode

        # traverse through the linked list
        else:
            # make sure next node is none i.e. make sure current node is the last node
            if self.nextNode:
                # make a recursive call to the function where parameters are
                # 'data' data that we want to delete and
                # 'self' which will act as the previousNode
                self.nextNode.removeRecursive(data, self)