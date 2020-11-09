# Exercise 5: Bottle Deposits

# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.


small_bottle_deposit = 0.10
large_bottle_deposit = 0.25

small_input = int(input("How many bottles with size one liter or less do you have?"))
large_input = int(input("How many bottles with size greater than one liter do you have?"))

refund = (small_input*small_bottle_deposit) + (large_input*large_bottle_deposit)

print("Your refund will be $"+ format(refund, '.2f'))
