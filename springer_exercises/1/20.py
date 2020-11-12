# Write a program that computes the amount of gas in moles when the user supplies
# the pressure, volume and temperature. Test your program by determining the number
# of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
# a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
# approximately 20 degrees Celsius or 68 degrees Fahrenheit.

# PV = nRT

R = 8.314
V = 12/1000
T = 273.15
P = 20000000

n = (P*V)/(R*T)
print(round(n,2), "moles of gas")
