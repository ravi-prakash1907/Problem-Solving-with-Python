############################################
##
##         Compound Interest
##
############################################


# scanning inputs

# getting principle amount
principle = float(input("Enter the principle amount: "))
# getting interest rate
rate = float(input("Enter the rate of interest, per year(in %): "))
# getting time 
duration = int(input("Enter total duration(in years): "))

# applying CI formula to find the final amount after applying 
# compound interest for given time duration
finalPayableAmt = round(principle * (pow((1 + rate/100), duration)), 2)

# finding the Compound Interest alone out of total amount
CI = round((finalPayableAmt - principle), 2) # rounded upto 2 decimal places

# output
print("\nCompound Interest is: ",CI) 


## O/P
##
## Enter the principle amount:  2390.76
## Enter the rate of interest, per year(in %):  11.20
## Enter total duration(in years):  3
##
## Compound Interest is:  896.62