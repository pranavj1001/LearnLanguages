class Stack:

    # constructor
    # here we initialize the list that will be used for the stack
    def __init__(self):
        self.stack = []

    # method to push element into the stack
    def push(self, data):
        self.stack.append(data)

    # method to pop topmost i.e. last element from the stack
    def pop(self):
        self.stack.pop()

    # method to find whether the stack is empty or not
    def isEmpty(self):
        if not self.stack:
            print("True")
        else:
            print("False")

    # method to find the current length of the stack
    def size(self):
        print(len(self.stack))

    # method to view the top most element
    def viewTop(self):
        if self.stack:
            print(self.stack[len(self.stack) - 1])
        else:
            print("There are no elements in the stack")

    # method to view the full stack
    def viewFullStack(self):
        for i in self.stack:
            print(i)