class Queue:

    # constructor
    # here we initialize the list that will be used for the queue
    def __init__(self):
        self.queue = []

    # method to push elements into queue
    def enqueue(self, data):
        self.queue.insert(0, data)

    # method to dequeue elements from the queue
    def dequeue(self):
        return self.queue.pop()

    # method to find the current length of the queue
    def size(self):
        print(len(self.queue))

    # method to find whether the queue is empty or not
    def isEmpty(self):
        if not self.queue:
            print("True")
        else:
            print("False")

    # method to view the top most element
    def viewTop(self):
        if self.queue:
            print(self.queue[len(self.queue) - 1])
        else:
            print("There are no elements in the queue")

    # method to view the full queue
    def viewFullQueue(self):
        for i in self.queue:
            print(i)