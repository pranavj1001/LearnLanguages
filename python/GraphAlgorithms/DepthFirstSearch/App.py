from Node import Node
from DFS import dfs

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

node1.neighbourList.append(node2)
node1.neighbourList.append(node3)
node2.neighbourList.append(node4)
node2.neighbourList.append(node5)
node3.neighbourList.append(node6)

dfs(node1)
