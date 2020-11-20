# Write a program that reads a position from the user. Use an if statement to deter-
# mine if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking.

square = "h8"

if square[0] in ['a','c','e','g']:
    first = 'b'
else:
    first = 'w'


row_flip = int(square[1]) % 2
if row_flip == 0:
    if first == 'w':
        first = 'black'
    else:
        first = 'white'

print(f"{square} is {first}")