# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.


r = 10
h = 15

pi = 3.14159265358979

area = pi*(r ** 2)
volume = area * h


print("Volume = ", format(volume, '.1f'))
