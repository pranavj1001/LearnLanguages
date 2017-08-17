from Node import Node

class TST(object):

    # constructor
    # initially rootNode points to None
    def __init__(self):
        self.rootNode = None

    # function to insert data into the TST
    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    # function to find the correct place to insert a value and key (one char at a time)
    def putItem(self, node, key, value, index):

        # get the character from the key
        # initially index is zero i.e. get the first char initially
        character = key[index]

        # if there's no node for the current character then create a new node
        if node is None:
            node = Node(character)

        # if the character has a lesser value than the current node then go left
        if character < node.char:
            node.leftNode = self.putItem(node.leftNode, key, value, index)

        # if the character has a greater value than the current node then go right
        elif character > node.char:
            node.rightNode = self.putItem(node.rightNode, key, value, index)

        # when the above two conditions are false
        # and we have not traversed through the entire characters of the key
        # then go middle
        elif index < len(key) - 1:
            node.middleNode = self.putItem(node.middleNode, key, value, index + 1)

        # insert the value here as we have traversed through the characters of the key
        else:
            node.value = value

        return node

    # function to get the value from the key
    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)

        if node is None:
            return None

        return node.value

    # function to find the correct place and fetch the value from the TST
    def getItem(self, node, key, index):

        # if there's no value i.e. key is incorrect
        if node is None:
            return None

        # get the character from the key
        # initially index is zero i.e. get the first char initially
        character = key[index]

        # if the character has a lesser value than the current node then go left
        if character < node.char:
            return self.getItem(node.leftNode, key, index)

        # if the character has a greater value than the current node then go right
        elif character > node.char:
            return self.getItem(node.rightNode, key, index)

        # when the above two conditions are false
        # and we have not traversed through the entire characters of the key
        # then go middle
        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index + 1)

        # return the node as we have traversed through the characters of the key
        else:
            return node
