# Define variables and their values
# Define variable cars with a value of 100
cars = 100
# Define variable space_in_a_car with a value of 4.0
space_in_a_car = 4.0
# Define variable drivers with a value of 30
drivers = 30 
# Define variable passengers with a value of 90
passengers = 90
# Define variable cars_not_driven with a value of cars - drivers
cars_not_driven = cars - drivers
# Define variable cars_driven with a value of drivers
cars_driven = drivers
# Define variable carpool_capacity with a value of cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Define variable average_passengers_per_car with a value of passengers / cars_driven
average_passengers_per_car = passengers / cars_driven

# Print the information from the variables above
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
