# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec-
# onds respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

from time import sleep
try:
    s = int(input("Please enter an integer number of seconds\n"))
except:
    print("Integers only. Try again")
    exit()

if s > 31557699:
    print("Why would you want this countdown to run for more than a year? Try again")
    exit()

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




i = 0
while s > -1:

    value = 0
    input = s
    output = {
        "days": 0,
        "hours": 0,
        "minutes": 0,
        "seconds": 0

    }

    while value <= input:
        for c in conversions:
            while conversions[c] <= input:
                input = input - conversions[c]
                output[c] = output[c] + 1
                value = value + conversions[c]
        if value == 0:
            break


    str_out = '\r'+"{:02d}:".format(output["days"]) + "{:02d}:".format(output["hours"]) + "{:02d}:".format(
        output["minutes"]) + "{:02d}".format(output["seconds"])
    # str_out = '\r'+str(s)
    print(str_out, end= '', flush= True)
    s = s -1


    sleep(1)

print("\nCountdown Complete.")