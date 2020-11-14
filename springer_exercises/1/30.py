# In this exercise you will create a program that reads a pressure from the user in kilo-
# pascals. Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.

kpa = 200

psi = kpa * 0.145
mmhg = kpa * 0.2953
atm = kpa * 0.009869

print(psi)
print(mmhg)
print(atm)