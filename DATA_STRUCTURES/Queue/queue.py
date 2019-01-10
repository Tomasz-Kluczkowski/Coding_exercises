class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0

    def size(self):
        return len(self.stack1)

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.is_empty():
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            top = self.stack2.pop()
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
            return top
        return None



