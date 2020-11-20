# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.

date = input("please enter a month and day in the format 'mmdd'")

holidays = {
    "0101":"New Year's Day",
    "0601":"Canada Day",
    "1225":"Christmas Day"

}

if date in holidays:
    print( f"{date} is {holidays[date]}")
else:
    print(date, "is not a holiday")