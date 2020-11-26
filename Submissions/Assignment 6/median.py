############################################
##
##         Median of Given Samples
##
############################################

from math import sqrt
myList =  [74, 72, 14, 23, 89, 65, 10, 85, 24, 80]

print("Sample space: ",myList)

myList.sort()
if len(myList)%2 == 0:
  median = myList[len(myList)//2-1] + myList[len(myList)//2]
else:
  median = myList[len(myList)//2]

print("Median: ",median)

## O/P
##
## Sample space:  [74, 72, 14, 23, 89, 65, 10, 85, 24, 80]
## Median:  137