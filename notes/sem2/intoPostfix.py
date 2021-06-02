def postfix_converter( expn ):
    
    # Write your code here
    tempStack = Stack()

    operator = ['+','-','/','*','^'] ## this arrangement must remain same
    braces = ['(',')']
    answer = ''

    for ch in expn:
      if ch not in operator:
        answer += ch
      elif ch in operator:
        if tempStack.peek():
          if operator.index(ch)//2 > operator.index(tempStack.peek())//2:   ## o/p priority
            tempStack.push(ch)
          else:
            popped = tempStack.pop()
            answer += popped
            tempStack.push(ch)
        else:
          tempStack.push(ch)
      else:
        continue
      
    while tempStack.peek():
      popped = tempStack.pop()
      answer += popped
    
    return answer
    
    
# Uncomment the following block of code for evaluation purpose


expn = input( "Enter the infix expression (no space between elements): " )
pf_expn = postfix_converter (expn)
print ( "Postfix expression = {}".format( pf_expn ) )


