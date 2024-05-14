class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None] * max_size
        self.top = -1  

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, data):
        if self.is_full():
            print("Stack overflow")
        else:
            self.top += 1
            self.arr[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        else:
            removed_data = self.arr[self.top]
            self.top -= 1
            return removed_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.arr[self.top]

# Example for usage check up 
my_stack = Stack(5)
my_stack.push(10)
my_stack.push(20)
print(my_stack.pop()) 
print(my_stack.peek())  
