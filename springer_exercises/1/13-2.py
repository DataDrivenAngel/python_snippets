# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.

original_input = 369

coins = {
    "loonie"  : 200,
    "toonie"  : 100,
    "quarter" : 25,
    "dime"    : 10,
    "nickle"  : 5,
    "penny"   : 1
}


change = {
    "loonie"  : 0,
    "toonie"  : 0,
    "quarter" : 0,
    "dime"    : 0,
    "nickle"  : 0,
    "penny"   : 0
}
value = 0
input = original_input


for c in coins:

    change[c] = input // coins[c]
    value = value + ((input // coins[c]) * coins[c])
    input = input % coins[c]



print ("input was", original_input)
print(change)
print("which totals:")
print (value)
