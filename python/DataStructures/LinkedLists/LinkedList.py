from Node import Node

class LinkedList(object):

    # constructor
    # here we will initialize current head and the counter
    def __init__(self):
        self.head = None
        self.counter = 0

    # O(1)  method to add elements at starting position
    def insertAtStart(self, data):

        # increment counter
        self.counter += 1

        # make a new node
        newNode = Node(data)

        # if we are inserting the first element to a linked list which no nodes till now
        if not self.head:
            # the head now points to the first element
            self.head = newNode

        # if we are inserting the first element to a linked list which already has > 0 nodes
        else:
            # the new node's nextnode now points to the previous node
            newNode.nextNode = self.head
            # the head now points to the first element
            self.head = newNode

    # O(1)  method to find number of elements of a linkedlist
    def size(self):
        print("Size ->", self.counter)

    # O(n)  method to insert a node at the end
    def insertAtEnd(self, data):

        # if the linked list didn't have any prior elements then call insertAtStart function
        if not self.head:
            self.insertAtStart(data)
            return

        # increment counter
        self.counter += 1

        # create a new node
        newNode = Node(data)
        # for traversing create a current node
        actualNode = self.head

        # traverse till we not reach the end
        while actualNode.nextNode:
            actualNode = actualNode.nextNode

        # now add the new node
        actualNode.nextNode = newNode

    # O(n)  method to add an element in a given position
    def insertAtPosition(self, data, position):

        # if user gave wrong values for the position
        if (position < 0) or (position > self.counter):
            print("Sorry can't add")

        # if user wants to add the element at start
        elif position == 0:
            self.insertAtStart(data)

        # logic to add elements in between
        else:

            # increment counter
            self.counter += 1

            # create a new node
            newNode = Node(data)
            # for traversing create a current node
            actualNode = self.head

            # traverse till we not reach the position
            for i in range(0, position-1):
                actualNode = actualNode.nextNode

            # temporary variable to hold the nextNode value
            temp = actualNode.nextNode

            # now add the new node
            actualNode.nextNode = newNode
            # update the nextNode value of the new node
            newNode.nextNode = temp

    # O(n)  method to remove an node
    def remove(self, data):

        # decrement counter
        self.counter -= 1

        # make sure that there are nodes in the linked list and start doesn't point to None
        if self.head:
            # if our luck shines and the start points to the node which we want to remove
            if data == self.head.data:
                # now head points to the next node
                self.head = self.head.nextNode

            # if start doesn't point to the node which we want to remove
            else:
                # call the function from Node.py
                self.head.removeRecursive(data, self.head)

    # O(n)  method to traverse through the linked list
    def traverseList(self):

        # for traversing create a current node
        actualNode = self.head

        # traverse through the linked list and print the nodes
        while actualNode:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode