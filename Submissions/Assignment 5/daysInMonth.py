############################################
##
##         Days in a Month
##
############################################

# number of days in given month

# list of months
months = "\n1) January \n2) February \n3) March \n4) April \n5) May \n6) June \n7) July \n8) August \n9) September \n10) October \n11) November \n12) December"

# taking input (year and month)
year = int(input("Enter the year: "))
month = int(input(months+"\n\nEnter a month number: "))

# validating month
if month >= 1 and month <= 12:
  if month != 2:
    if month in (1,3,5,7,8,10,12):
      print("Month has 31 days.")
    else:
      print("Month has 30 days.")
  # checking for leap year
  elif (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print("Month has 29 days.")
  else:
    print("Month has 28 days.")
else:
  print("Invalid month!!")

## O/P
##
## Enter the year: 2020
## 
## 1) January 
## 2) February 
## 3) March 
## 4) April 
## 5) May 
## 6) June 
## 7) July 
## 8) August 
## 9) September 
## 10) October 
## 11) November 
## 12) December
## 
## Enter a month number: 2
## Month has 29 days.