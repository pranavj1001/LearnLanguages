from Node import Node

class DisjointSet(object):

    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)

    def find(self, node):
        currentNode = node

        while currentNode.parentNode:
            currentNode = currentNode.parentNode

        root = currentNode
        currentNode = node

        while currentNode is not root:
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp

        return root.nodeID

    def union(self, node1, node2):

        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]

        if root1.height < root2.height:
            root1.parentNode = root2
        elif root1.height > root2.height:
            root2.parentNode = root1
        else:
            root2.parentNode = root1
            root1.height += 1

        self.setCount -= 1

    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes), None)
        vertex.parentNode = node
        self.rootNodes.append(node)
        self.setCount += 1
        self.nodeCount += 1