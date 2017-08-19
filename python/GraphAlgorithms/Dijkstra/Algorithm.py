class Algorithm(object):

    # Logic to calculate the shortest path
    def calculateShortestPath(self, startVertex):

        # initialize an empty queue
        queue = []
        # the minimum distance to the root vertex is 0 and push it in the queue
        startVertex.minDistance = 0
        queue.insert(0, startVertex)

        # loop till there are vertices in the queue
        while queue:

            # pop the element the from the queue
            currentVertex = queue.pop()

            # traverse through the adjacent edges of the vertex
            # since dijkstra follows greedy approach,
            # it finds global optimum from local minimum
            for edge in currentVertex.neighbourList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                # if minimum distance is discovered then
                # the startVertex of the current edge becomes the predecessor of the targetVertex
                # the minimum distance to reach the targetVertex is updated
                # since we just reached the targetVertex, hence add it to the queue
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    queue.insert(0, v)

    # Method to print the the shortest path to the target
    def getShortestPathTo(self, targetVertex):

        print("Shortest path to target is: ", targetVertex.minDistance)

        node = targetVertex

        while node:
            print("%s -> " %node.name)
            node = node.predecessor