# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3 + 1 + 4 + 1 = 9.


number = str(1234)
s = 0
for element in number:
    s = s + int(element)


print("Sum:",s)