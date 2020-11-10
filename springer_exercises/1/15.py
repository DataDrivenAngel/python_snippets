# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

input = 250 #ft

inch_to_ft = 1/12
mile_to_ft = 5280
yard_to_ft = 3

inches = input/inch_to_ft
yards = input/yard_to_ft
miles = input/mile_to_ft

print("inches:",inches, "yards:", yards, "miles:", miles)