class Vertex(object):

    # constructor
    # provides the basic structure of the vertex
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbourList = []
