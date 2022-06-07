"""This is the solution script for the IT-647 Week 7 assignment - Michael Mesnikoff"""
#
# We will calculate the factorial for a user-input integer.
# This script will include better input validation.
#

# Import the math library.
import math

#
# pos_int()
#   no arguments
#   returns a single positive integer
#
# Create a reuseable function to prevent entering anything other than
# a poaitive integer.  Generate an error message if anything else is entered.
# Keep iterating until a positive integer is entered.  Return the integer.
#
def pos_int():
    # Create a "flag".
    x = 0

    # Begin the repeating loop to get the user's input.
    while(x == 0):
        # Get the user's input
        user_input = input("Enter a positive integer: ")

        # First, check for anything other than numeric data.
        try:
            the_int = int(user_input)
            
            # Assuming we passed the the first check, now check for 0 or negative.
            if (the_int == 0):
                print("Input cannot be 0. Please try again.")
            elif(the_int < 0):
                print("Input cannot be negative. Please try again.")
            # If everything passes, return the integer.
            else:
                return(the_int)
            
        # catch exception if cannot be converted
        except ValueError:
            print("Only numeric data is acceptable.  No alphabetics or other characters.")
            print("Please try again.")

        # If we got to here restart the loop


#
# gen_factorial(int)
#   accepts one positive integer argument
#   returns a single integer value
#
# A recursive (self-calling) method to generate a factorial value.
#
def gen_factorial(the_int):
    #
    # Very simple here.  If the input integer is down to 1, we are done, so return.
    # Otherwise, run the recursion again until we reach 1.
    # Just following the widely available formula here.
    #
    if (the_int == 1):
        return(the_int)
    else:
        return (the_int * gen_factorial(the_int - 1)) 
    # End of gen_factorial() method
    
        
#
# Here is the 'main' function.
# Show a basic prompt, call the method to get the user's input, then call the method
# to generate the factorial value.  Print the result.
#
print("\nInput a single positive integer when prompted, to generate a factorial value.")
sum_total = 0
sum_total = pos_int()

# Just being tricky here, saving an extra variable.
print("The factorial of", sum_total, end = '')

# Call the factorial generating method, with an intial total of 0.
sum_total = gen_factorial(sum_total)
print(" is: ", sum_total)
