import heapq

class Algorithm(object):

    def calculateShortestPath(self, startVertex):

        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue, startVertex)

        while queue:

            currentVertex = heapq.heappop(queue)

            for edge in currentVertex.neighbourList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue, v)

    def getShortestPathTo(self, targetVertex):

        print("Shortest path to target is: ", targetVertex.minDistance)

        node = targetVertex

        while node:
            print("%s -> " %node.name)
            node = node.predecessor