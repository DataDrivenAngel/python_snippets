# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

days = 2s
hours = 1
minutes = 1
seconds = 1

hours = hours + (days * 24)
minutes = minutes + (hours * 60)
seconds = seconds + (minutes *60)

print(seconds)
