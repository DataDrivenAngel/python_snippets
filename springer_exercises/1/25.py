# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec-
# onds respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

s = 242999

conversions = {
    "days": 86400,
    "hours": 3600,
    "minutes": 60,
    "seconds" : 1



}

output = {
    "days"    : 0,
    "hours"   : 0,
    "minutes" : 0,
    "seconds" : 0

}

value = 0
input = s

while value <= input:
    for c in conversions:
         while conversions[c] <= input:
            input = input - conversions[c]
            output[c] = output[c] +1
            value = value + conversions[c]

print ("input was", s)
print(output)

print("{:02d}:".format(output["days"])+"{:02d}:".format(output["hours"])+"{:02d}:".format(output["minutes"])+"{:02d}".format(output["seconds"]))
