# Exercise 8: Widgets and Gizmos

# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

weight_widget = 75
weight_gizmo = 112

gizmos = int(input("enter gizmo count"))
widgets = int(input("enter widget count"))

gizmo_weight_total = weight_gizmo*gizmos
widget_weight_total = weight_widget*widgets
total = gizmo_weight_total+widget_weight_total
print("total:",total, "grams")
