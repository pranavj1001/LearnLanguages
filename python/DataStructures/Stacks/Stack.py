class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        if self.stack == []:
            print("True")
        else:
            print("False")

    def size(self):
        print(len(self.stack))

    def viewTop(self):
        if self.stack != []:
            print(self.stack[len(self.stack) - 1])
        else:
            print("There are no elements in the stack")

    def viewFullStack(self):
        for i in self.stack:
            print(i)