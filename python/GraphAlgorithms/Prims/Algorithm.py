import heapq

class Algorithm(object):

    # constructor
    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.edgeHeap = []
        self.fullCost = 0

    # Method to construct a spanning tree
    def constructSpannigTree(self, vertex):

        # remove the root node from the unvisited list
        self.unvisitedList.remove(vertex)

        # while there are elements in the unvisited list
        while self.unvisitedList:

            # traverse through every adjacent edges of the current vertex
            # if the the target vertex of the edge is in the unvisited list
            # then add it to the heap
            for edge in vertex.neighbourList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge)

            # get the min edge
            minEdge = heapq.heappop(self.edgeHeap)

            # append it to the tree and print the edge
            self.spanningTree.append(minEdge)
            print('%s - %s' % (minEdge.startVertex.name, minEdge.targetVertex.name))

            # calculate the full cost i.e. cost of the minimum cost tree
            self.fullCost += minEdge.weight

            # update the vertex for next instance of the while loop
            # and also update it from the unvisited list
            vertex = minEdge.targetVertex
            self.unvisitedList.remove(vertex)