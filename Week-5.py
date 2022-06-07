"""This is the solution script for the IT-647 Week 5 assignment - Michael Mesnikoff"""
# Import the math library.
import math

# First, create the list as given in the instructions.
Data = [0, -1, 2, -3, 4, -5, 6, -7, 8]

# Create a variable, initialized to 0, to hold the sum.
the_sum = 0

# Now, loop through the list and add the values together.
for the_value in Data:
    the_sum += the_value

# Now, print the sum.
print('The sum of the list values is: ', the_sum)

# Re-initialize th sum value
the_sum = 0

# Next, loop through the list and add the absolute values together.
for the_value in Data:
    the_sum += abs(the_value)

# Now, print the absolute values sum.
print('The sum of the absolute values of the list values is: ', the_sum)
