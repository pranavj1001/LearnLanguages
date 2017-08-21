from Vertex import Vertex
from Edge import Edge
from Algorithm import Algorithm

vertex1 = Vertex("A")
vertex2 = Vertex("B")
vertex3 = Vertex("C")
vertex4 = Vertex("D")

edge1 = Edge(1, vertex1, vertex2)
edge2 = Edge(1, vertex1, vertex3)
edge3 = Edge(100, vertex1, vertex4)
edge4 = Edge(1, vertex3, vertex4)
edge5 = Edge(0.1, vertex2, vertex4)

vertex1.neighbourList.append(edge1)
vertex1.neighbourList.append(edge2)
vertex1.neighbourList.append(edge3)
vertex3.neighbourList.append(edge4)
vertex2.neighbourList.append(edge5)

unvisitedList = [vertex1, vertex2, vertex3, vertex4]

algorithm = Algorithm(unvisitedList)
algorithm.constructSpannigTree(vertex1)