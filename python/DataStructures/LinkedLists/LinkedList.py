from Node import Node

class LinkedList(object):

    # constructor
    def __init__(self):
        self.head = None
        self.counter = 0

    # O(1)
    def insertAtStart(self, data):

        self.counter += 1

        newNode = Node(data)

        # if we are inserting the first element
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # O(1)
    def size(self):
        print("Size ->", self.counter)

    # O(n)
    def insertAtEnd(self, data):

        if not self.head:
            self.insertAtStart(data)
            return

        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    # O(n)
    def remove(self, data):

        self.counter -= 1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.removeRecursive(data, self.head)

    # O(n)
    def traverseList(self):
        actualNode = self.head

        while actualNode:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode