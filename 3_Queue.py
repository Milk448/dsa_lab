from 2_stack import as Stack,
class ImportedStack:
     self.item=[]
     def addElementAtEnd(self, data):
          self.item.append(item)


     def removeFromFront(self):
          if self.item !=0:
               return self.item.pop()
     def peek(self, data):
          if self.item!=None:
               return self.item[index]
          
     def check_is_empty(self):
          if self.item==0:
               return True
          else:
               return False




#This an other way I implemented the    Queue 
class Queue:
    def __init__(self):
         self.data = []
    
    def enqueue(self, data):
         self.data.append(data)

    def Is_empty(self):
         if self.Is_empty==0:
              return None 
         else:
              return len(self.data)
    
    def dequeue(self):
         if self.Is_empty==0:
              return None
         else:
              return self.data.pop(0)
    
    def peek(self):
         if self.Is_empty!=0:
              return self.data[0]
         else:
              return None
         
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.Is_empty()) 
print(my_queue.peek())  # Output: Bob
print(my_queue.dequeue())  # Output: Bob
print(my_queue.dequeue())  # Output: Charlie
print(my_queue.Is_empty())
print(my_queue.dequeue())  # Output: None (empty queue)
print(my_queue.Is_empty()) 
print(my_queue.Is_empty()) 
print(my_queue.Is_empty()) 
print(my_queue.Is_empty()) 




