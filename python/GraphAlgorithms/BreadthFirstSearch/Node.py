class Node(object):

    # constructor
    def __init__(self, name):
        self.name = name
        self.neighbourList = []
        self.visited = False