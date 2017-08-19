import sys

class Vertex(object):

    # constructor
    # provides the basic structure of the vertex
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.neighbourList = []
        # initially minDistance = the largest positive integer supported by the platform’s Py_ssize_t type
        self.minDistance = sys.maxsize