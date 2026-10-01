
class MyQueue:

    def __init__(self):
        self.ins = []
        self.outs = []

    def push(self, x):
        self.ins.append(x)

    def pop(self):
        self.move()
        return self.outs.pop()

    def peek(self):
        self.move()
        return self.outs[-1]

    def empty(self):
        return not self.ins and not self.outs

    def move(self):
        if not self.outs:
            while self.ins:
                self.outs.append(self.ins.pop())