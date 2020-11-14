# Write a program that begins by reading the air temperature and wind speed from the
# user. Once these values have been read your program should display the wind chill
# index rounded to the closest integer.

temp = -10
speed = 10

wci = 13.12 + (0.6215 * temp) \
      - (11.37 * (speed ** 0.16)) \
      + (0.3965 * ((temp)**0.16))


print(wci)