class Algorithm(object):

    # boolean variable to store value for cycles
    HAS_CYCLE = False

    # Logic to calculate the shortest path
    def calculateShortestPath(self, vertexList, edgeList, startVertex):

        # the minimum distance to the root vertex is 0
        startVertex.minDistance = 0

        # loop for number of vertices times
        for i in range(0, len(vertexList) - 1):

            # go through all the edges
            # major difference between dijkstra and bellman ford
            for edge in edgeList:

                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                # if minimum distance is discovered then
                # the startVertex of the current edge becomes the predecessor of the targetVertex
                # the minimum distance to reach the targetVertex is updated
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        # go through the edges once more to look for cycles
        for edge in edgeList:

            if self.hasCycle(edge):
                print("Negative Cycle detected")
                Algorithm.HAS_CYCLE = True
                return

    # Logic to find the cycle in the graph
    def hasCycle(self, edge):
        if edge.startVertex.minDistance + edge.weight < edge.targetVertex.minDistance:
            return True
        else:
            return False

    # Method to print the the shortest path to the target
    def getShortestPathTo(self, targetVertex):

        if not Algorithm.HAS_CYCLE:
            print("Shortest path to target is: ", targetVertex.minDistance)

            node = targetVertex

            while node:
                print("%s -> " %node.name)
                node = node.predecessor