from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        self.queue2.put(value)

        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()

stack = StackUsingQueue()
output = []
stack.push(1)
stack.push(2)
output.append(str(stack.pop()))
stack.push(3)
output.append(str(stack.pop()))
output.append(str(stack.pop()))

print(", ".join(output))
