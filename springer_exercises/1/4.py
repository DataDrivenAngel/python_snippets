# Exercise 4: Area of a Field

# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

length = float(input("enter length in feet"))
width = float(input("enter width in feet"))

area = length * width
acre_to_sqft = 43560

area_in_acres = area/acre_to_sqft

print ("the field is", area_in_acres, "acres!")