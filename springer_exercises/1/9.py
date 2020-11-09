# Exercise 9: Compound Interest

# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

interest_rate = 0.04

balance = float(input("Enter the number of dollars you have"))

y1 = balance+ (balance*interest_rate)
y2 = y1+(y1*interest_rate)
y3 = y2+(y2*interest_rate)

y1_display = "$"+str(format(y1, '.2f'))
y2_display = "$"+str(format(y2, '.2f'))
y3_display = "$"+str(format(y3,'.2f'))
print(y1_display, '\n', y2_display, '\n', y3_display)