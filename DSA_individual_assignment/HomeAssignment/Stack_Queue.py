class Stack:
    def __init__(self, capacity):
        # Initialize the stack with a fixed capacity
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def push(self, item):
        # Add an item to the top of the stack
        if self.isFull():
            raise Exception("Stack overflow")
        self.top += 1
        self.array[self.top] = item

    def pop(self):
        # Remove and return the top item from the stack
        if self.isEmpty():
            raise Exception("Stack underflow")
        item = self.array[self.top]
        self.top -= 1
        return item

    def peek(self):
        # Return the top item without removing it
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.array[self.top]

    def isEmpty(self):
        # Check if the stack is empty
        return self.top == -1

    def isFull(self):
        # Check if the stack is full
        return self.top == self.capacity - 1

class QueueUsingStacks:
    def __init__(self, capacity):
        # Initialize two stacks for the queue
        self.stack1 = Stack(capacity)
        self.stack2 = Stack(capacity)

    def enqueue(self, item):
        # Add an item to the end of the queue
        if self.stack1.isFull() and self.stack2.isFull():
            raise Exception("Queue overflow")
        self.stack1.push(item)

    def dequeue(self):
        # Remove and return the front item from the queue
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            raise Exception("Queue underflow")
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        # Return the front item without removing it
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            raise Exception("Queue is empty")
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

# Testing the QueueUsingStacks class
queue = QueueUsingStacks(5)

# Enqueue several items into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("Enqueued items: 10, 20, 30, 40, 50")

# Perform peek operations
print("Peek:", queue.peek())  # Should output 10

# Dequeue some items from the queue
print("Dequeued:", queue.dequeue())  # Should output 10
print("Dequeued:", queue.dequeue())  # Should output 20

# Perform peek operations
print("Peek:", queue.peek())  # Should output 30

# Continue dequeueing
print("Dequeued:", queue.dequeue())  # Should output 30
print("Dequeued:", queue.dequeue())  # Should output 40
print("Dequeued:", queue.dequeue())  # Should output 50

# Try to dequeue from an empty queue
try:
    print("Dequeued:", queue.dequeue())
except Exception as e:
    print(e)  # Should output "Queue underflow"

# Try to peek in an empty queue
try:
    print("Peek:", queue.peek())
except Exception as e:
    print(e)  # Should output "Queue is empty"
