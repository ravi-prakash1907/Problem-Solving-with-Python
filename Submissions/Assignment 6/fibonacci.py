############################################
##
##         Print 'n' Fibonacci Terms
##
############################################

num = int(input("Enter the upper bound: ")) # number of terms
a = 0
b = 1

if num >= 2:
  print("\nFirst " + str(num) + "fibonacci terms are: ")
  print(a, b, end = " ")
  for i in range(2,num):
    c = a + b
    a = b
    b = c
    print(c, end = " ")
elif num == 1:
  print(a)
else:
  print("Invalid input!!")

## O/P
##
## Enter the upper bound: 7
## 
## First 7 fibonacci terms are: 
## 0 1 1 2 3 5 8 