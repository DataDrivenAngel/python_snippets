# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

sides = 9

assert sides >= 3, "That's a line or dot. Enter at least three sides"
assert sides <= 10, "more than ten sides is too many"

shapes = {
    3: "triangle",
    4: "quadrilateral",
    5: "pentagon",
    6: "hexagon",
    7: "heptagon",
    8: "octagon",
    9: "nonagon",
    10: "decagon"

}

print(shapes[sides])