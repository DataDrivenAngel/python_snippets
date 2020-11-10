# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.

ft = 12     # inch
inch = 2.54 # cm

input_ft = 6
input_inch = 2

inch = input_inch + (input_ft * ft)
cm = inch*2.54

print(cm)