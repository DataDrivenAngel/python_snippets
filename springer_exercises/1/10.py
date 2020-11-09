# Exercise 10: Arithmetic
#
# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# The quotient when a is divided by b
# The remainder when a is divided by b
# The result of log 10 a
# The result of a^b

import math
a,b = input("enter two integer values seperated by a space").split()
a = int(a)
b = int(b)

print("You entered a:", a, "b:", b)
print ("Sum:", (a+b))
print ("difference", (a-b))
print ("product:", (a*b))
print ("quotient:", (a / b))
print ("remainder:", (a % b))
print ("log10 of a:", (math.log10(a)))
print ("A^B", (a ** b))