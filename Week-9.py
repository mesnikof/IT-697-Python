"""This is the solution script for the IT-647 Weeks 9 and 10
   Final Project assignment - Michael Mesnikoff"""
#
# Create the random number guessing game.
#

# Import the os, math, and random libraries.
import os
import math
import random

#
# generate_random(int, int)
#
# input arguments - 2 integer values
# return - 1 integer value
#
# Generates and returns pseudo-random number with a value between arg1 and arg2, inclusive.
#
def generate_random(min_limit, max_limit):
    return(random.randrange(min_limit, max_limit, 1))
#
# End of funtion generate_random
#


#
# user_guess(int, int, int)
#
# input arguments - 3 integer values
# return - 1 integer value
#
# A reuseable function to prevent entering anything other than
# an integer within the allowable range.  Generate an error message if anything else is entered.
# Keep iterating until a valid integer is entered.  Return the integer.
#
def user_guess(min_limit, max_limit, count):
    # Create a "flag".
    x = 0

    # Begin the repeating loop to get the user's input.
    while(x == 0):
        # Get the user's input
        print("Guess ", (count + 1), ":")
        user_input = input("Enter an integer between %d and %d (inclusive): " % (min_limit, max_limit))

        # First, check for anything other than numeric data.
        try:
            the_int = int(user_input)
            
            # Assuming we passed the the first check, now check for limits.
            if ((the_int < min_limit) or (the_int > max_limit)):
                print("Input out of range. Please try again.")
            # If everything passes, return the integer.
            else:
                return(the_int)
            
        # catch exception if cannot be converted
        except ValueError:
            print("Only numeric data is acceptable.  No alphabetics or other characters.")
            print("Please try again.")

        # If we got to here restart the loop
#
# End of function user_guess()
#


#
# Here is the 'main' function.
# Show a basic prompt, call the method to get the user's input, then call the method
# to generate the factorial value.  Print the result.
#

# Create a variable initialized to the maximum number of guesses.
GUESS_LIMIT = 7

# Create the minimum and maximum limits for the random number.
MIN = -100
MAX = 100

# Generate thw random number to be guessed by calling the generate_random() function.
random_number = generate_random(MIN, MAX)

# Get the current username from the OS.
username = os.getlogin()

# Show a welcome message with the allowed number of guesses.
print("Welcome, %s, to the number guessing game.  You are allowed %d guesses.  Good luck.\n" % (username, GUESS_LIMIT))

# Use a 'for' loop to prompt the user for guesses.  End the loop on success or guess limit.
for count in range (GUESS_LIMIT):
    # Call the user_guess() function.
    the_guess = user_guess(MIN, MAX, count)

    # Compare the guess to the number, show "higher" or "lower".
    if (the_guess < random_number):
        print("low guess\n")
        # Set count to 99 to signal failure if this was the last guess.
        if (count == (GUESS_LIMIT - 1)):
            count = 99
    elif (the_guess > random_number):
        print("high guess\n")
        # Set count to 99 to signal failure if this was the last guess.
        if (count == (GUESS_LIMIT - 1)):
            count = 99
    else:
        print("Correct guess. Congratulations %s!\n" % (username))

        # Update the game report file.
        # First, call the open() function to open the game report file.
        # This is done in Append+, Text mode.  Creates the file if it doesn't
        # exist.  Opens it positioned at the end for appending additional text
        # if it does, and allows for later reading, if needed. Text mode.
        #
        # This is done in a try/except block to catch file open failures.
        # Report if this happens.
        try:        
            fileHandle = open("Game_Report.txt", "a+t")
        except:
            print("Unable to open file \"Game_Report.txt\"")
        else:
            # If we got to here the file was successfully opened.
            # Perform the update.  Write a pseudo-JSON format.
            fileHandle.write("\n{{user:%s},{guesses:%d}}" % (username, (count + 1)))
            fileHandle.close()
        break

    # End of the 'for' loop.

# To finish the game, if the user failed (count == 99), write the message.
# Then say goodbye.
if (count == 99):
    print("Sorry, you were unable to guess %d in %d guesses." % (random_number, GUESS_LIMIT))

print("Please play again.  Goodbye...\n")
#
# End of script
#
