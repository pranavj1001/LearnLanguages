from Vertex import Vertex
from Edge import Edge
from Algorithm import Algorithm

# create the vertices
vertexA = Vertex("A")
vertexB = Vertex("B")
vertexC = Vertex("C")
vertexD = Vertex("D")
vertexE = Vertex("E")
vertexF = Vertex("F")
vertexG = Vertex("G")
vertexH = Vertex("H")

# create the edges
edge1 = Edge(5, vertexA, vertexB)
edge2 = Edge(8, vertexA, vertexH)
edge3 = Edge(9, vertexA, vertexE)
edge4 = Edge(15, vertexB, vertexD)
edge5 = Edge(4, vertexB, vertexH)
edge6 = Edge(12, vertexB, vertexC)
edge7 = Edge(6, vertexH, vertexF)
edge8 = Edge(7, vertexH, vertexC)
edge9 = Edge(5, vertexE, vertexH)
edge10 = Edge(4, vertexE, vertexF)
edge11 = Edge(20, vertexE, vertexG)
edge12 = Edge(9, vertexD, vertexG)
edge13 = Edge(3, vertexC, vertexD)
edge14 = Edge(11, vertexC, vertexG)
edge15 = Edge(1, vertexF, vertexC)
edge16 = Edge(13, vertexF, vertexG)

# define the relation between the edges and vertices
vertexA.neighbourList.append(edge1)
vertexA.neighbourList.append(edge2)
vertexA.neighbourList.append(edge3)
vertexB.neighbourList.append(edge4)
vertexB.neighbourList.append(edge5)
vertexB.neighbourList.append(edge6)
vertexH.neighbourList.append(edge7)
vertexH.neighbourList.append(edge8)
vertexE.neighbourList.append(edge9)
vertexE.neighbourList.append(edge10)
vertexE.neighbourList.append(edge11)
vertexD.neighbourList.append(edge12)
vertexC.neighbourList.append(edge13)
vertexC.neighbourList.append(edge14)
vertexF.neighbourList.append(edge15)
vertexF.neighbourList.append(edge16)

vertexList = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG, vertexH]
edgeList = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16]

# apply Bellman-Ford algorithm
bellmanFord = Algorithm()
bellmanFord.calculateShortestPath(vertexList, edgeList, vertexA)
bellmanFord.getShortestPathTo(vertexG)

# to try a cycle example uncomment the code given below
# edge1 = Edge(1, vertexA, vertexB)
# edge2 = Edge(1, vertexB, vertexC)
# edge3 = Edge(1, vertexC, vertexD)
# edge4 = Edge(-15, vertexC, vertexB)
# edge5 = Edge(300, vertexA, vertexD)
#
# vertexA.neighbourList.append(edge1)
# vertexA.neighbourList.append(edge2)
# vertexB.neighbourList.append(edge3)
# vertexC.neighbourList.append(edge4)
# vertexC.neighbourList.append(edge5)
#
# vertexList = [vertexA, vertexB, vertexC, vertexD]
# edgeList = [edge1, edge2, edge3, edge4, edge5]
#
# bellmanFord = Algorithm()
# bellmanFord.calculateShortestPath(vertexList, edgeList, vertexA)
# bellmanFord.getShortestPathTo(vertexD)