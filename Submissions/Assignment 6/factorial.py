#########################
##
##         Factorial
##
########################

num = int(input("Enter a positive number: "))
counter = 1

if num < 0:
  print("Factorial of '"+str(num)+"' is a complex number!!")
else:
  fact = 1
  while counter <= num:
    fact *= counter
    counter += 1
  print("Factorial of '"+str(num)+"' is ("+str(num)+"!): ",fact)

## O/P
##
## Enter a positive number: 9
## Factorial of '9' is (9!):  362880