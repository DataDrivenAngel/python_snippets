# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

Tc = 20

Tk = Tc + 273.15
Tf = Tc * 1.8 + 32

print(str(Tc)+'C', str(Tk)+'K', str(Tf)+'F')