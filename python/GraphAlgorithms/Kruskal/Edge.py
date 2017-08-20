class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority