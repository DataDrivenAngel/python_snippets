# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that must be
# added or removed to achieve the desired temperature change.

mass = 20000
dt = 80

print("mass in grams is: ", mass, "\nDesired temperature change in degrees C is:", dt)

C = 4.186

energy = mass*C*dt

print("The energy required to increase the sample by ", dt, "degrees is", energy, " Joules")

j_to_kwh = (1/36000000)
cost_per_kwh = 0.089

cost = energy * j_to_kwh * cost_per_kwh

print("The cost is $" + format(cost, '.2f'))