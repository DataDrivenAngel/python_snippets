# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the level is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table.

db = 58

noises = {
    130: "Jackhammer",
    106: "Gas Lawnmower",
    70: "Alarm Clock",
    40: "Quiet Room"
}

if db in noises:
    print(f"{db} db is the volume of an {noises[db]}")
elif db > max(noises):
    print(f"{db} db is louder than the sound of a {noises[max(noises)]}")
elif db < min(noises):
    print(f"{db} db is quieter than the sound of a {noises[min(noises)]}")
else:
    keys = list(noises.keys())
    n = 0
    for key in keys:
        if db < keys[n] and db > keys[n+1]:
            print(f"{db} db is louder than a {noises[keys[n+1]]} and quieter than a {noises[keys[n]]}")
        n = n +1