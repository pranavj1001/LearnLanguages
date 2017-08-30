from DisjointSet import DisjointSet

class Algorithm(object):

    # Method to construct a spanning tree
    def constructSpanningTree(self, vertexList, edgeList):

        disjointSet = DisjointSet(vertexList)
        spanningTree = []

        edgeList.sort()

        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex

            # check whether the edges don't form a cycle
            # if they don't then add the edge to the spanning tree
            # and union the two nodes
            if disjointSet.find(u.parentNode) != disjointSet.find(v.parentNode):
                spanningTree.append(edge)
                disjointSet.union(u.parentNode, v.parentNode)

        # print the spanning tree by printing all the edges
        for edge in spanningTree:
            print(edge.startVertex.name, "-", edge.targetVertex.name)