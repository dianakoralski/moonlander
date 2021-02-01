""" Module tests Project 1 functions
CPE 101

Section: 03-2208

Project 1 Tests

Name: Diana Koralski

Cal Poly User: dkoralsk@calpoly.edu
"""
from moonlander import *

# tests for functions that calculate

# tests for update_acceleration(gravity, fuel_rate) function
assert update_acceleration(1.62, 2) == -.97
assert update_acceleration(1.62, 5) == 0
assert update_acceleration(1.62, 7) == .65

# tests for update_altitude(altitude, velocity, acceleration) function
assert update_altitude(5, 5, 5) == 12.5
assert update_altitude(2, 5, -15) == -0.5
assert update_altitude(4, 6, -5) == 7.5

# tests for update_velocity(velocity, acceleration) function
assert update_velocity(1,2) == 3
assert update_velocity(4,-2) == 2
assert update_velocity(3,0) == 3

# tests for update_fuel(fuel, fuel_rate) function
assert update_fuel(1,2) == -1
assert update_fuel(8,2) == 6
assert update_fuel(5,3) == 2

# tests for functions that do I/O

# test for show_welcome() function
assert show_welcome() == "Welcome to the Moon Lander Simulation!"

# test for get_fuel() function
fuel = 5
assert get_fuel() == 5

# test for get_altitude() function
altitude = 100
assert get_altitude() == 100

#test for display_state(time, altitude, velocity, fuel, fuel_rate) function
time = 0
altitude = 5
velocity = 4
fuel = 3
fuel_rate = 2
assert display_state(time, altitude, velocity, fuel, fuel_rate) == "time=0, altitude=5.00, velocity=4.0, fuel=3, fuel rate=2"

# test for get_fuel_rate(fuel) function
fuel_rate = 4
assert get_fuel_rate(7) == 4

#tests for display_landing_status(velocity) function
assert display_landing_status(-1) == "Status at landing - The eagle has landed!"
assert display_landing_status(-5) == "Status at landing - Enjoy your oxygen while it lasts!"
assert display_landing_status(-15) == "Status at landing - Ouch - that hurt!"

