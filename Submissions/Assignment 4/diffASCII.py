################################################################
##
##  Diff. b/w ascii code of upper and lower case (same) letter
##
################################################################


# getting the charector
char1 = input("Enter you fevorate alphabet: ")

# checking that user has entered only single alphabet or not
if len(char1) == 1 and char1.isalpha():
    # finding the other varient of the same alphabet
    if char1.islower():
        char2 = char1.upper()
    else:
        char2 = char1.lower()
    
    # finding differance 
    diff = abs(ord(char1)-ord(char2))
    print("Differance between Upper and Lower case ASCII values of your fav. charector is: ",diff)
else:
    print("Invalid input!!")


## O/P
##
## Enter you fevorate alphabet:  a
## Differance between Upper and Lower case ASCII values of your fav. charector is:  32
