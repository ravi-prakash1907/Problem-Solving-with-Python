class Node:
    def __init__(self, value = None):
        self.data = value
        self.nextNode = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.listSize = 0
        
    def push(self, value):
        newNode = Node(value)
        newNode.nextNode = self.head 
        self.head = newNode 
        self.listSize += 1
        
    def pop(self):
        if self.head is not None:
          popped = self.peek()
          self.head = self.head.nextNode
          self.listSize -= 1
          return popped
        
    def size(self):
        return self.listSize
        
    def peek(self):
        if self.head is not None:
          return self.head.data


# When you are ready, uncomment this block

# Do not edit anything below this line

A = Stack() # Initiate the stack
A.push("Value 01") # push values
A.push("Value 02")
print("Size={}".format(A.size())) # check the size of stack
print("Top element is {}".format(A.peek())) # display the top element of stack
c = A.pop() # pop elements in stack, store the removed element in a variable if required
A.push("Value 03")
A.push(c)
# Popping all elements from the stack:
while A.size() > 0:
   print( A.pop() )
   
