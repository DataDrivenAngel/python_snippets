# Write a program that reads a year from the user and displays the animal associated
# with that year. Your program should work correctly for any year greater than or equal
# to zero, not just the ones listed in the table

animals = [
    "Dragon",
    "Snake",
    "Horse",
    "Sheep",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Hare"
]

input_year = 2005

year = (input_year - 2000) % 12
# 2000 = year of the dwagon

print(f"year {input_year} is the year of the {animals[year]} !")