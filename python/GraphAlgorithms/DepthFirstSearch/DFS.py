def dfs(node):

    node.visited = True
    print("%s -> " % node.name)

    # use recursion to traverse through the nodes
    for i in node.neighbourList:
        if not i.visited:
            dfs(i)