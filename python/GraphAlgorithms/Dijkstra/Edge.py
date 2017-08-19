class Edge(object):

    # constructor
    # provides the basic structure of the edge
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex