# Develop a program that reads the lengths of the sides of a triangle from the user and
# displays its area.

import math

s1 = 2
s2 = 2
s3 = 2

s = (s1+s2+s3)/2
sqrt = int(s * (s-s1) * (s-s2) * (s-s3))
area = math.sqrt(sqrt)

print(area)
