# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed.


month = "february"



months = {
    "january" : 31,
    "february" : "28 days in a common year and 29 days in a leap year",
    "march"     : 31,
    "april"     : 30,
    "may"       : 31,
    "june"      : 30,
    "july"      : 31,
    "august"    : 31,
    "september" : 30,
    "october"   : 31,
    "november"  : 30,
    "december"  : 31,

}

if month == "february":
    print(f"{month} has {months[month]}")
else:
    print(f"{months[month]} days in {month}")
