# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.

age = int(input("enter integer number of years"))

assert age >= 0, "Please enter a positive nubmer of years"

if age <= 2:
    human_age = age *10.5
else:
    human_age = 21 + ((age-2)*4)
print(f"{age} human years is {float(human_age)} dog years")