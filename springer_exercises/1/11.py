# In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
# gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPG to L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.


liter_per_gal = 3.7854
km_per_mile = 1.6093

#convert from

# m/g * km/m = km/g
# km/g * l/g = km/l
# 1/(km/l) * 100 km = L/100km

mpg = int(input("mpg?"))
kmg = mpg * km_per_mile
kml = kmg / liter_per_gal

l100km = (1/kml) * 100
print("L/100k =" , format(l100km,'.3f'))


