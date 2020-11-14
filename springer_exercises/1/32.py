# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

ints = [2,20,9]


print("Mid:",sum(ints)-max(ints)-min(ints))
print("Max:",max(ints))
print("Min:",min(ints))

