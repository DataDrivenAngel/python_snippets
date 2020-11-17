# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

l1 = 4
l2 = 4
l3 = 4

if l1 == l2 and l2 == l3:
    print("You've got an equilateral triangle there!")

elif l1 != l2 and l2 != l3 and l1 != l3:
    print("Scalene triangle. boring")

else:
    print("Looks like an isoceles triangle")

