# Exercise 6: Tax and Tip

# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

price = float(input("Enter Meal Price"))
tax_rate = 0.05
tip_rate = 0.18


tax = price * tax_rate
tip = price * tip_rate
grand_total = price+tax+tip

display_tax = str(format(price * tax_rate, '.2f'))
display_tip = str(format(price * tip_rate, '.2f'))
display_price = str(format(price, '.2f'))
display_grand_total = str(format(grand_total,'.2f'))

print("Meal price  : $"
      +display_price
      +"\nTax Total   : $"
      +display_tax+"\nTip Total   : $"
      +display_tip+"\nGrand Total : $"
      +display_grand_total)