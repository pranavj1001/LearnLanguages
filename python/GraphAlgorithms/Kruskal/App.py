from Vertex import Vertex
from Edge import Edge
from Algorithm import Algorithm

vertex1 = Vertex("A")
vertex2 = Vertex("B")
vertex3 = Vertex("C")
vertex4 = Vertex("D")
vertex5 = Vertex("E")
vertex6 = Vertex("F")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(4, vertex1, vertex4)
edge3 = Edge(4, vertex2, vertex3)
edge4 = Edge(4, vertex2, vertex4)
edge5 = Edge(3, vertex2, vertex5)
edge6 = Edge(1, vertex2, vertex6)
edge7 = Edge(5, vertex3, vertex6)
edge8 = Edge(2, vertex4, vertex5)
edge9 = Edge(5, vertex5, vertex6)

vertexList = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6]

edgeList = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9]

algorithm = Algorithm()
algorithm.constructSpanningTree(vertexList, edgeList)