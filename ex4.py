#!/usr/bin/env python
# ex.4.py page 45
# Declaring the variable 'cars' 
# = (single quotation)or equals to use to assign the value 
# Datatype of the variable is integer

cars = 100
# space_in_car variable having the data in floating type
# _ (under score)/dash is used to presume as space in between
# variable
space_in_a_car = 4.0
drivers = 30
passengers = 90
# Here we are doing subtraction and assigning the variable

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, " drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
print("")

