############################################
##
##         Transpose of a Matrix
##
############################################

## 

myMatrix = []

#rows = inr("Enter number of rows in the matrix: ")
#cols = inr("Enter number of columns in the matrix: ")
rows = 4
cols = 3

counter = 1
for i in range(4):
  temp = []
  for j in range(3):
    temp.append(counter)
    counter += 1
  myMatrix.append(temp)

rows = len(myMatrix)
cols = len(myMatrix[0])

transposeMatrix = []

for i in range(cols):
  temp = []
  for j in range(rows):
    temp.append(myMatrix[j][i])
  transposeMatrix.append(temp)


print("\nMain Matrix:")
for i in myMatrix:
  for j in i:
    print(j, end = " ")
  print()

print("\nTranspose Matrix:")
for i in transposeMatrix:
  for j in i:
    print(j, end = " ")
  print()


## O/P
##
## Main Matrix:
## 1  2  3 
## 4  5  6 
## 7  8  9 
## 10 11 12 
## 
## Transpose Matrix:
## 1 4 7 10 
## 2 5 8 11 
## 3 6 9 12 