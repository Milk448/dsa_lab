class Node:
    #initializing of the node class with function which takes data.
    #at this stage it takes two things -1) data and-2)pointer to the next node  
    def __init__(self, data):
        self.data = data
        self.next = None


#this below is singly linked list class which its initialize the linked list and perofrms various operation on singly linked list 
class LinkedList:
    def __init__(self):
        self.head = None
#at this I implemeted function which takes data and inset that data into specified position 
    def insertAtPos(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                raise Exception("Position out of bounds")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
#at this I implemeted function which deletes from specified position 
    def deleteAtPosition(self, pos):
        if self.head is None:
            raise Exception("List is empty")
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None or temp.next is None:
                raise Exception("Position out of bounds")
            temp = temp.next
        if temp.next is None: #this deletes the pointer of the the deleted data, if this is not done there will be two linkedlist which we don't need  
            raise Exception("Position out of bounds")
        temp.next = temp.next.next
        
#Deletes the node that occurs after the node with the specified prev_node_data.
    def deleteAfterNode(self, prev_node_data):
        temp = self.head
        while temp is not None:
            if temp.data == prev_node_data:
                if temp.next is not None:
                    temp.next = temp.next.next
                else:
                    raise Exception("No node exists after the given node")
                return
            temp = temp.next
        raise Exception("Node with given data not found")
#Searches for a node with the specified value and returns its position.
    def searchNode(self, key):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
        return -1
    




#AT this I implemented stack using linkedlist 
class Stack:
    def __init__(self):  #initializing stack 
        self.head = None

    def push(self, data):   #this function help us to add element from back/ at end 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):    # this functiion implemented for retuning the value at back(end) adn then delete it if its  not empty 
        if self.head is None:
            raise Exception("Stack underflow")
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def peek(self):
        if self.head is None:
            raise Exception("Stack is empty")
        return self.head.data

# Testing the LinkedList class
ll = LinkedList()
ll.insertAtPos(1, 1)
ll.insertAtPos(2, 2)
ll.insertAtPos(3, 3)
ll.insertAtPos(4, 2)

print("After inserts:")
current = ll.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

ll.deleteAtPosition(2)

print("After deleting at position 2:")
current = ll.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

ll.deleteAfterNode(3)

print("After deleting node after node with data 3:")
current = ll.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

print(f"Search for node with value 3: Position {ll.searchNode(3)}")
print(f"Search for node with value 5: Position {ll.searchNode(5)}")

# Testing the Stack class
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element is:", stack.peek())
print("Popped element is:", stack.pop())
print("Top element after pop is:", stack.peek())
