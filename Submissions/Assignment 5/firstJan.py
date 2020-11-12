############################################
##
##         Day on 1st January
##
############################################

## day on 1st Jan of given year

# 01/01/1900  --->  Monday
initYear = 1900
finalYear = int(input("Year: ")) # because this years' only first day is needed

leapYears = (finalYear - initYear)//4
if checkLeapYear(finalYear):
  leapYears -= 1

totalDaysPassed = (finalYear - initYear)*365 + leapYears

day = (totalDaysPassed)%7

print("Day on 01/01/"+str(finalYear)+": ",end='')

if day == 0:
  print("Monday")
elif day == 1:
  print("Tuesday")
elif day == 2:
  print("Wednesday")
elif day == 3:
  print("Thursday")
elif day == 4:
  print("Friday")
elif day == 5:
  print("Saturday")
elif day == 6:
  print("Sunday")

## O/P
##
## Year: 2021
## Day on 01/01/2021: Friday