# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).

h = 10

G = 9.8
v = 0
import math
v_final = math.sqrt((v ** 2) + (2*G*h))
print("Final Velocity is:", v_final, "M/S")