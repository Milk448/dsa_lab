class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()  

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]  

    def is_empty(self):
        return len(self.items) == 0  

# my usage 

print(my_stack.pop())  # Output should be : Pencil (LIFO)
print(my_stack.peek())  
print(my_stack.pop())  
print(my_stack.pop())  
print(my_stack.pop())   # I have checked it also 
