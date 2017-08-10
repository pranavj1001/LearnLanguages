class Heap(object):
    # Heap's size
    HEAP_SIZE = 10

    # constructor
    # here we initialize the heap and the currentPosition
    def __init__(self):
        self.heap = [0] * Heap.HEAP_SIZE
        self.currentPosition = -1

    # Logic to add elements to an heap
    def insert(self, data):
        # if heap is full then don't insert the element and return
        if self.isFull():
            print("Heap is Full")
            return

        # increase the currentPosition
        self.currentPosition = self.currentPosition + 1
        # add the data
        self.heap[self.currentPosition] = data
        # check whether the newly added element satisfies the conditions of an heap
        self.fixUp(self.currentPosition)

    # Logic to order elements in an heap when a new element is added
    def fixUp(self, index):

        # find the currentNode's parent index number i.e. position of its parent node
        parentIndex = int((index - 1) / 2)

        # since this is a max heap, so swap elements whenever an element larger than its parent node is found
        # if you want the heap to be min heap then simply comment the above line and uncomment the below line
        # while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            index = parentIndex
            parentIndex = int((index - 1) / 2)

    # method to display the heap
    def displayHeap(self):

        if (self.heap):
            for i in self.heap:
                print(i)
        else:
            print("Heap is empty")

    # Method to find out whether the heap is full or not
    # used when a new element is added
    def isFull(self):

        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False
