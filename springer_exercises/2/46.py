# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

import datetime

day =354


seasons = {
    80: "Spring",
    173: "Summer",
    266: "Fall",
    356: "Winter"
}


if day < min(seasons):
    print(f"That's {seasons[356]}")
elif day >= max(seasons):
    print(f"That's {seasons[356]}")
else:
    keys = list(seasons.keys())
    n = 0
    for key in keys:
        if day >= keys[n] and day < keys[n+1]:
            print(f"day {day} is in {seasons[key]}")
        n = n +1