from . import Node

class LinkedList(object):

    # constructor
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        newNode = Node(data)

        # if we are inserting the first element
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode