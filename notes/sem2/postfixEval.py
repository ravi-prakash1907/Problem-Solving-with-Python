class Stack:
    
    # Write your code here
    ## node
    class Node:
      def __init__(self, value = None):
          self.data = value
          self.nextNode = None
    
    ## main stack class
    def __init__(self):
        self.head = None
        self.listSize = 0
        
    def push(self, value):
        newNode = Node(value)
        newNode.nextNode = self.head 
        self.head = newNode 
        self.listSize += 1
        
    def pop(self):
        if self.head is None:
          return False
        if self.head is not None:
          popped = self.peek()
          self.head = self.head.nextNode
          self.listSize -= 1
          return popped
        
    def peek(self):
        if self.head is not None:
          return self.head.data
        else:
          return False
    
def postfix_evaluator( expn ):
    
    # Write your code here
    operandStack = Stack()
    operatorStack = Stack()
    mainStack = Stack()
    answer = None

    for ch in expn:
      mainStack.push(ch)

    operator = ['+','-','/','*','^']
    answer = 0

    while mainStack.peek():
      popped = mainStack.pop()
      if popped in operator:
        operatorStack.push(popped)
        
      else:
        operandStack.push(int(popped))
    
    answer = operandStack.pop()
    while operandStack.peek():
      op = operatorStack.pop()
      answer = eval('{}{}{}'.format(answer, op, operandStack.pop()))
    
    return answer
    
    
# Uncomment the following block of code for evaluation purpose

#'''
expn = input( "Enter the postfix expression (elements separated by space): " )
value = postfix_evaluator (expn)
print ( "The value of the expression = {}".format( value ) )

#'''
