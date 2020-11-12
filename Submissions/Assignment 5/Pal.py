############################################
##
##         Palindrome or Not
##
############################################

## given 4-digit number is palindrome or not

num = int(input("Enter a 4 digit number: "))

# findig reverse
once = (num%10)*1000
num //= 10

tens = (num%10)*100
num //= 10

hundreds = (num%10)*10
num //= 10

thousands = (num%10)
num //= 10

reverse = once + tens + hundreds + thousands
##########

if num == reverse:
  print(num,"is palindrome!")
else:
  print(reverse,"is NOT palindrome!")

## O/P
##
## Enter a 4 digit number: 2341
## 1432 is NOT palindrome!