############################################
##
##         Character Detector
##
############################################

# problem: write a program to check whether the entered character is 
# lower case or upper case.

char = input("Enter a character: ")

if ord(char) >= 65 and ord(char) <= 90:
  print("You entered an upper case alphabet!")
elif ord(char) >= 97 and ord(char) <= 122:
  print("You entered a lower case alphabet!")
elif ord(char) >= 48 and ord(char) <= 57:
  print("You entered a number!")
else:
  print("You entered a special character!")

## O/P
##
## Enter a charecter: *
## You entered a special cherector!