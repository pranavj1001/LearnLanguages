class Algorithm(object):

    HAS_CYCLE = False

    def calculateShortestPath(self, vertexList, edgeList, startVertex):
        startVertex.minDistance = 0

        for i in range(0, len(vertexList) - 1):
            for edge in edgeList:

                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:

            if self.hasCycle(edge):
                print("Negative Cycle detected")
                Algorithm.HAS_CYCLE = True
                return

    def hasCycle(self, edge):
        if edge.startVertex.minDistance + edge.weight < edge.targetVertex.minDistance:
            return True
        else:
            return False

    def getShortestPathTo(self, targetVertex):

        if not Algorithm.HAS_CYCLE:
            print("Shortest path to target is: ", targetVertex.minDistance)

            node = targetVertex

            while node:
                print("%s -> " %node.name)
                node = node.predecessor