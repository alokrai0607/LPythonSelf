class QueueUsingStack:
    
    
    
    def __init__(self):
       
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
       
        self.enqueue_stack.append(value)


    def dequeue(self):
        
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        if not self.dequeue_stack:
            return None

        return self.dequeue_stack.pop()



# Input
queue = QueueUsingStack()
output = []
queue.enqueue(1)
queue.enqueue(2)
output.append(str(queue.dequeue()))
queue.enqueue(3)
output.append(str(queue.dequeue()))
output.append(str(queue.dequeue()))

# Output
print(", ".join(output))
