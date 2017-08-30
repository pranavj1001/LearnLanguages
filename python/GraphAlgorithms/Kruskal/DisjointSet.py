from Node import Node

class DisjointSet(object):

    # constructor
    # provides the basic structure of the union find data structure
    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)

    # find() operation traverses up from node to find root.
    # The idea of path compression is to make the found root as parent of node
    # so that we don’t have to traverse all intermediate nodes again.
    def find(self, node):
        currentNode = node

        while currentNode.parentNode:
            currentNode = currentNode.parentNode

        # naive implementation
        # return currentNode.nodeID

        # path compression technique used below
        root = currentNode
        currentNode = node

        while currentNode != root:
            temp = currentNode.parentNode
            currentNode.parentNode = root # path compression
            currentNode = temp

        return root.nodeID

    # Logic to do union of two sets
    def union(self, node1, node2):

        index1 = self.find(node1)
        index2 = self.find(node2)

        # if the nodes are in the same set then return
        if index1 == index2:
            return

        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]

        # Attach smaller height tree under root of high height tree
        if root1.height < root2.height:
            root1.parentNode = root2
        elif root1.height > root2.height:
            root2.parentNode = root1
        else:
            root2.parentNode = root1
            root1.height += 1

        self.setCount -= 1

    # Method to make sets for every vertex
    # in this algo, vertex refers to the vertex of the graph
    # and node refers to the node of the sets
    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes), None)
        vertex.parentNode = node
        self.rootNodes.append(node)
        self.setCount += 1
        self.nodeCount += 1