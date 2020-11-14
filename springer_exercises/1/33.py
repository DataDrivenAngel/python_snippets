# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. All of the
# values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

price = 349
discount = 0.4

n = 12

order_price = price*n
order_final_price = order_price * discount

print(f"Price:${price/100 :02}")
print(f"Discount:{(1-discount)*100}%")
print(f"Total: ${order_price/100 :02}")
print(f"Grand Total: ${order_final_price/100 :02}")