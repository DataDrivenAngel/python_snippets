# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the table  An appropriate error message should be displayed
# if no such note exists.
#     

bills = {
    1: "GW",
    2: "TJ",
    5: "Abe",
    10: "Musical dude",
    20: "Andrew Jackass",
    50: "Grant",
    100: "Benjamin"
}




bill = 100

assert bill in bills, "That's not real money!!!!"
print(f"{bill} = {bills[bill]} ")


