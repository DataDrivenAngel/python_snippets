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
    "seconds": 1
                }
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

    str_out = '\r' + f"{output['days']:02}:{output['hours']:02}:{output['minutes']:02}:{output['seconds']:02}"
    # str_out = '\r'+str(s)
    print(str_out, end='', flush=True)
    s = s - 1

    sleep(1)

print("\nCountdown Complete.")

