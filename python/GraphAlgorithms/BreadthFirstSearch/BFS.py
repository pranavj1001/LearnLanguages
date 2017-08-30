# initialize a list to implement a queue
queue = []

def bfs(node):

    # set the root node's visited property to be true
    node.visited = True
    queue.append(node)

    # while there's an element in a queue
    while queue:

        # pop the element and print it
        node = queue.pop()
        print("%s -> " % node.name)

        # traverse through the neighbours of a node
        for i in node.neighbourList:
            if not i.visited:
                i.visited = True
                # insert the node at the first position
                queue.insert(0, i)