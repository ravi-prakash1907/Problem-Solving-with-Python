############################################
##
##      Check for Armstrong Number
##
############################################

num = int(input("Enter a positive number: "))
yourNum = num

length = 0
digits = []
if num > 0:
  while num != 0:
    length += 1
    digits.append(num % 10)
    num //= 10


newNum = 0
i = 0
while i < len(digits):
  newNum += pow(digits[i], 3)
  i += 1

if newNum == yourNum:
  print(yourNum,"is an armstrong number!")
else:
  print(yourNum,"is NOT an armstrong number!")

## O/P
##
## Privide the cofficients of the quadratic equation -
## 
## Enter a positive number: 153
## 153 is an armstrong number!