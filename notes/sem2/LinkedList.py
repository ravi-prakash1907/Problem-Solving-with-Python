# Define a linked list
class Node:
    def __init__(self, value = None):
        self.data = value
        self.nextNode = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.listSize = -1
    
    def append(self, val):
        newNode = Node(val)
        if self.head is None:
          self.head = newNode
        else:
          last = self.head
          while(last.nextNode):
            last = last.nextNode
          last.nextNode = newNode
        self.listSize += 1
        return
        
    def insert(self, pos, val):
        if pos <= self.listSize+1:
          newNode = Node(val)
          if pos == 0:
            newNode.nextNode = self.head # points to node that was head earlier
            self.head = newNode # making new node as head
            self.listSize += 1
            return
      
          currNode=self.head
          currPos=0
          while currNode is not None:
            if pos == currPos+1:
              newNode.nextNode = currNode.nextNode
              currNode.nextNode = newNode
              self.listSize += 1
              return
            else:
              currPos+=1
            
    def size(self):
        return self.listSize+1
        
    def seek(self, pos):
        pos -= 1
        if self.listSize >= pos:
          currNode=self.head
          currPos=0
          if currPos == pos:
            return currNode.data
          else:
            currNode = currNode.nextNode
            currPos += 1
        return
        
    def display(self):
        print("---")  # Do not change this
        
        temp = self.head
        while(temp):
          print(temp.data)
          temp = temp.nextNode
        
        print("---")  # Do not change this
        
    def pop(self, pos=None):
        pos = self.listSize if pos is None else pos-1
        
        if self.listSize >= pos:
          if pos == 0:
            self.head = self.head.nextNode
          else:
            count = 1
            temp = self.head
            while count < pos:
              temp = temp.nextNode
              count += 1
            temp.nextNode = temp.nextNode.nextNode
          
          self.listSize -= 1
        return
        
    # End of class LinkedList


# Do not change anything below this point

A = LinkedList() # create an empty linked list
A.append("Value 01") # add a node with value "Value 01" to the end of the linked list
A.insert(0, "Value 02") # Insert an element at position 0, with value = "Value 02"
print( f"size={A.size()}" ) # print the size of the linked list A.
print( f"Element at Position 1= {A.seek(1)}" ) # display the element at certain position
A.display() # Display the elements in A
A.insert(1, "Value 03")
A.insert(3, "Value 04")
A.display()
A.pop(2) # Remove node at position 1
A.pop() # Remove the last node
A.display()

