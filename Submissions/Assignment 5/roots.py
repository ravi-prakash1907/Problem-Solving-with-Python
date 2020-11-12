############################################
##
##      Root of a Quadratic Equation
##
############################################

from math import sqrt

print("Privide the cofficients of the quadratic equation -\n") 

a = int(input("Value of 'a':"))
b = int(input("Value of 'b':"))
c = int(input("Value of 'c':"))

print("\nYour equation:\n"+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0")

if a == 0:
  print("\nRoots doesn't exist!!")
else:
  forRoot = pow(b,2) - 4*a*c
  if forRoot < 0:
    print("\nRoots are imaginary!!")
  else:
    root1,root2 = (-b - int(sqrt(pow(b,2) - 4*a*c)))/(2*a), (-b + int(sqrt(pow(b,2) - 4*a*c)))/(2*a)
    print("\nRoot 1: ",root1, "\nRoot 2: ",root2)

## O/P
##
## Privide the cofficients of the quadratic equation -
## 
## Value of 'a':2
## Value of 'b':5
## Value of 'c':2
## 
## Your equation:
## 2x^2 + 5x + 2 = 0
## 
## Root 1:  -2.0 
## Root 2:  -0.5