"""
Assignment 2: The Cost of Driving

Author: Kirti Subramanian
CWID: 20531478
Date: 10/9/2022

Program Description: This program will first ask the user for their car's fuel efficiency, the price
per gallon of gas for their car, and how many gallons are left in their car right now. Next, it calculates
the cost for driving 100 miles in addition to calculating how many miles the car can go given the number of
gallons it has left. The program will then print the original inputted values back to the user in sentence
form. Then it will also print the new calculated values in sentence form. The purpose is for the final printed
output to inform the user further about their car given some information that they provide.
"""

# This receives input from the user about 3 values and stores those input values into 3 respective variables.
mpg = int(input("What is the fuel efficiency of your car (in miles per gallon)? "))
gas_price = float(input("What is the price per gallon of gas for your car? "))
current_fuel = int(input("What is the number of gallons of gas currently in the tank of your car? "))

# These are the calculations that the program does in order to yield the 2 new values. These 2 new values are stored
# in 2 new variables.
cost_for_100 = "%.2f" % (gas_price * 100)
miles_left = mpg * current_fuel

# This is the output that will be returned to the user based on the values they initially gave and based on the
# program's calculations.
print()
print(f"The fuel efficiency of your car is {mpg} miles per gallon.")
print(f"The price per gallon of gas for your car is ${gas_price}.")
print(f"Your car currently has {current_fuel} gallons in its tank.")
print(f"The cost of the gas when you drive 100 miles is ${cost_for_100}.")
print(f"Your car can go {miles_left} miles with the gas that is currently in the tank.")

# first run
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment2.py
What is the fuel efficiency of your car (in miles per gallon)? 25
What is the price per gallon of gas for your car? 4.099
What is the number of gallons of gas currently in the tank of your car? 5

The fuel efficiency of your car is 25 miles per gallon.
The price per gallon of gas for your car is $4.099.
Your car currently has 5 gallons in its tank.
The cost of the gas when you drive 100 miles is $409.90.
Your car can go 125 miles with the gas that is currently in the tank.

Process finished with exit code 0

"""

# second run
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment2.py
What is the fuel efficiency of your car (in miles per gallon)? 40
What is the price per gallon of gas for your car? 3.799
What is the number of gallons of gas currently in the tank of your car? 10

The fuel efficiency of your car is 40 miles per gallon.
The price per gallon of gas for your car is $3.799.
Your car currently has 10 gallons in its tank.
The cost of the gas when you drive 100 miles is $379.90.
Your car can go 400 miles with the gas that is currently in the tank.

Process finished with exit code 0

"""