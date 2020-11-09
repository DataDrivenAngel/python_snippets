# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.
import math
from geopy import distance

# lat_in_1  = 52.2296756
# lat_in_2  = 52.406374
# long_in_1 = 21.9122287
# long_in_2 = 16.9251681

lat_in_1  = float(input("Lat1"))
lat_in_2  = float(input("Long1"))
long_in_1 = float(input("Lat2"))
long_in_2 = float(input("Long2"))



lat1 = math.radians(lat_in_1)
lon1 = math.radians(long_in_1)

lat2 = math.radians(lat_in_2)
lon2 = math.radians(long_in_2)

dist = 6371.01 * math.acos(
    math.sin(lat1) * math.sin(lat2) +
    math.cos(lat1) * math.cos(lat2) * math.cos(lon1-lon2)
)

print(dist)

coord_1 = (lat_in_1,long_in_1)
coord_2 = (lat_in_2,long_in_2)
print(distance.distance(coord_1,coord_2).km)
