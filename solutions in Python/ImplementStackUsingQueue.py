class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def empty(self):
        return True if len(self.stack) == 0 else False