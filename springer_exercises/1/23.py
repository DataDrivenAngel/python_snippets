# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.

import math
s = 4
n = 4
pi = 3.14159265358979

a = ((n*(s **2))/(4*math.tan(pi/n)))
print(a)
