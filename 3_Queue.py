from stack import Stack
class Queue:
    def __init__(self):
        self.s1 = Stack(max_size=10)  # Stack for enqueue operations
        self.s2 = Stack(max_size=10)  # Stack for dequeue operations

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None

        # Move elements from s1 to s2 if s2 is empty
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

        # Dequeue from s2 (FIFO)
        return self.s2.pop()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        # Move elements from s1 to s2 if s2 is empty (to maintain order)
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

        return self.s2.peek()

# Example usage
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
print(my_queue.dequeue())  # Output: 10
print(my_queue.peek())  # Output: 20
