###############################################
##
##      Hypotenuse of a Right Triangle
##
################################################


# importing the square root function
from math import sqrt

# getting base
base = int(input("Base of given right-triangle: "))
# getting height
height = int(input("Height of given right-triangle: "))

# finding hypotenuous using formula
hypotenuse = sqrt(pow(base,2) + pow(height,2))

# printing the result
print("\nHypotenuse of the of given right-triangle is: ",hypotenuse,"units")



## O/P
##
## Base of given right-triangle:  3
## Height of given right-triangle:  4

## Hypotenuse of the of given right-triangle is:  5.0 units