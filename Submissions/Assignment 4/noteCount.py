###############################################
##
##      minimize number of notes
##
################################################



# scaning input (total amount)
totalAmount = int(input("Enter total amount of money: "))

# init every note count
hundrads =0
fifties = 0
twenties = 0
tens = 0
fives = 0
twos = 0
ones = 0

## counting every note
if (totalAmount // 100) != 0:
    hundrads = totalAmount//100
    totalAmount %= 100
else:
    print("Can not hold a note of 100")

if (totalAmount // 50) != 0:
    fifties = totalAmount//50
    totalAmount %= 50
else:
    print("Can not hold a note of 50")

if (totalAmount // 20) != 0:
    twenties = totalAmount//20
    totalAmount %= 20
else:
    print("Can not hold a note of 20")

if (totalAmount // 10) != 0:
    tens = totalAmount//10
    totalAmount %= 10
else:
    print("Can not hold a note of 10")

if (totalAmount // 5) != 0:
    fives = totalAmount//5
    totalAmount %= 5
else:
    print("Can not hold a note of 5")

if (totalAmount // 2) != 0:
    twos = totalAmount//2
    totalAmount %= 2
else:
    print("Can not hold a note of 2")

ones = totalAmount
if ones == 0:
    print("Can not hold a note of 1")

# total notes
noteCount = hundrads + fifties + twenties + tens + fives + twos + ones

print("\nTotal notes needed: ",noteCount)


############################################

## O/P
## 
## Enter total amount of money: 1255
## Can not hold a note of 20
## Can not hold a note of 10
## Can not hold a note of 2
## Can not hold a note of 1
## 
## Total notes needed:  14