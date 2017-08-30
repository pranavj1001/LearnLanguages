class Node(object):

    # constructor
    # provides the basic structure of the node
    def __init__(self, height, nodeID, parentNode):
        self.height = height
        self.nodeID = nodeID
        self.parentNode = parentNode