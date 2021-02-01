""" Module implements Project 1 functions
CPE 101

Section: 03-2208

Project 1 Functions

Name: Diana Koralski

Cal Poly User: dkoralsk@calpoly.edu
"""

class Moonlander:
    """Moonlander
    Attributes:
        altitude (float): the distance from the surface of the moon.
        fuel (int): the fuel
        velocity (float): It is positive when the Moonlander is moving away from the moon.
        acceleration (float):  It is positive when the Moonlander is moving away from the moon.
    """

    def __init__(self, alt, fuel):
        """Gives altitude and fuel of moonlander.

        Args:
            alt (float): altitude of moonlander
            fuel (int): fuel of moonlander.
        """
        self.alt = alt
        self.fuel = fuel
        self.acceleration = 0
        self.velocity = 0

# show_welcome() function
def show_welcome():
    """Displays welcome message.
    Returns:
        str: prints welcome message
    """
    message = "Welcome to the Moon Lander Simulation!"
    print(message)
    return message

# get_fuel() function
def get_fuel():
    """Prompts user for a positive integer.
    Returns:
        int: positive integer
        str: error message
    """
    while True:
        fuel = int(input("Please enter initial fuel amount [a positive number]: "))
        if fuel > 0:
            break
        print("%d is not a positive number!" % (fuel))
    return fuel

# get_altitude() function
def get_altitude():
    """Prompts user for a positive integer between 1 and 9999.
    Returns:
        int: positive integer from 1 to 9999
        str: error message
    """
    while True:
        altitude = int(input("Please enter initial altitude [1, 9999]: "))
        if 0 < altitude < 10000:
            break
        print("%d is not a value between 1 and 9999!" % (altitude))
    return altitude

# display_state(time, altitude, velocity, fuel, fuel_rate) function
def display_state(time, altitude, velocity, fuel, fuel_rate):
    """Displays the state of the moonlander for the given parameters.
    Args:
        time (int): the time the moonlander has been landing.
        altitude (float): tha altitude of the moon lander from the moon.
        velocity (float): the velocity at which the moon lander is travelling towards the moon.
        fuel (int): the fuel left in the moonlander.
        fuel_rate (int): the rate at which the fuel is used up.
    Returns:
        str: returns a string in format "time=%d, altitude=%.2f, velocity=%.1f, fuel=%d, \
        fuel rate=%d"
    """
    ret = "time=%d, altitude=%s, velocity=%s, fuel=%d, fuel rate=%d" \
     % (time, altitude, velocity, fuel, fuel_rate)
    print(ret)
    return ret

# get_fuel_rate(fuel) function
def get_fuel_rate(fuel):
    """Prompts user for a positive integer between 0 and 10 that decides how much fuel to use.
    Args:
        fuel (int):amount of fuel used from lunar lander.
    Returns:
        int: the amount of fuel remaining on the lunar lander.
        str: error message
    """
    while True:
        fuel_rate = int(input("Please enter fuel rate [0, 9]: "))

        if 0 <= fuel_rate < 10:
            break
        print("%d is not a number between 0 and 9!" % (fuel_rate))
    return min(fuel_rate, fuel)

# display_landing_status(velocity) function
def display_landing_status(velocity):
    """Displays the landing status of the moonlander for velocity of the moonlander at landing.
    Args:
        velocity (float): the velocity ofthe moon lander at landing in meters per second.
    Returns:
        str: returns a string describing the landing status of the moonlander based on its \
        velocity at landing.
    """
    status = "Status at landing - "
    if -1 <= velocity <= 0:
        status += "The eagle has landed!"
    elif -10 < velocity < -1:
        status += "Enjoy your oxygen while it lasts!"
    elif velocity <= -10:
        status += "Ouch - that hurt!"
    print(status)
    return status

# Functions that calculate

# update_acceleration(gravity, fuel_rate) function
def update_acceleration(gravity, fuel_rate):
    """Calculates the new acceleration at that time
    Args:
        gravity (float): the gravity of the moon (1.62).
        fuel_rate (int): the rate at which the moonlander's fuel is used.
    Returns:
        float: returns the new acceleration of the moonlander based on the formula acceleration = \
        gravity * ((fuel_rate / 5) - 1)
    """
    acceleration = gravity * ((fuel_rate / 5) - 1)
    return round(acceleration, 2)

# update_altitude(altitude, velocity, acceleration) function
def update_altitude(altitude, velocity, acceleration):
    """Calculates the new altitude at that time
    Args:
        altitude (float): the altitude of the moonlander from the moon.
        velocity (float): the velocity of the moonlander.
        acceleration (float): the acceleration of the moonlander.
    Returns:
        float: returns the new altitude of the moonlander based on the formula altitude = altitude \
         + velocity + (acceleration / 2).
    """
    altitude = altitude + velocity + (acceleration / 2.0)
    return round(altitude, 2)

# update_velocity(velocity, acceleration) function
def update_velocity(velocity, acceleration):
    """Calculates the new velocity at that time
    Args:
        velocity (float): the velocity of the moonlander.
        acceleration (float): the acceleration of the moonlander.
    Returns:
        float: returns the new velocity of the moonlander based on the formula velocity = velocity \
         + acceleration.
    """
    velocity = velocity + acceleration
    return round(velocity, 2)

# update_fuel(fuel, fuel_rate) function
def update_fuel(fuel, fuel_rate):
    """Calculates the new amount of fuel left
    Args:
        fuel (int): the velocity of the moonlander.
        fuel_rate (int): the acceleration of the moonlander.
    Returns:
        int: returns the new fuel amount of the moonlander based on the formula \
        fuel = fuel - fuel_rate.
    """
    return fuel - fuel_rate

def main():
    """ Runs MoonLander Simulation
    """
    show_welcome()
    alt = get_altitude()
    fuel = get_fuel()
    ml = Moonlander(alt, fuel)
    gravity = 1.62
    time = 0
    fuel_rate = 0
    display_state(time, ml.alt, ml.velocity, ml.fuel, fuel_rate)
    while ml.alt > 0:
        time = time + 1
        if ml.fuel > 0:
            fuel_rate = get_fuel_rate(fuel)
        else:
            fuel_rate = 0
        ml.fuel = update_fuel(ml.fuel, fuel_rate)
        ml.acceleration = update_acceleration(gravity, fuel_rate)
        ml.alt = update_altitude(ml.alt, ml.velocity, ml.acceleration)
        ml.velocity = update_velocity(ml.velocity, ml.acceleration)
        display_state(time, ml.alt, ml.velocity, ml.fuel, fuel_rate)

    display_landing_status(ml.velocity)

main()

