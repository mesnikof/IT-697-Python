"""This is the solution script for the IT-647 Week 6 assignment - Michael Mesnikoff"""
#
# This script gets the filename of a text file (we are just trusting it to be text format
# at this time), opens the file for reading (or returns an error message if this fails),
# and then counts the number of words and sentences in the file, returning these values
# to the user, with appropriate labels.
#
# Note: A couple of basic assumptions are made.
#   1) This script is VERY basic.  As it is unclear if such modules as "nltk" (natural
#       language toolkit) will be available wherever this script is run, the text "slicing"
#       method must be very simple using only the standard Python libraries/modules.
#   2) All sentences end with the punctuation marks ".", "?", or "!".  As such, any other
#       "non-standard" sentence structure will be ignored, and therefore miscounted).
#   3) "Words" are any length string of alphabetic characters, including "conected"
#       punctuation.  Thus, hyphenated strings and apostrophed strings will be counted as
#       single words.
#   4) Abbreviations, such as Mr. Mrs. Ms. and etc. will likely cause "miscounting of the
#       number of sentences.  Correction for this issue will require the creation of an
#       extensive "library" of abbreviations to avoid, as well as likely requiring the use
#       of the nltk library for total avoidance.  Should any of these abbreviations exist in
#       the test file, there may be sentence counting innacuracies.
#   5) Purely numeric strings should not be counted as words, but due to the basic method
#       of word slicing will be counted as words by this script.
#   6) Should "rewriting" be required for greater accuracy, use of regular expressions and
#       natural language checking be considered.
#

# Import the re, sys, and math libraries.
import re  #regular expressions
import sys #system
import math

# Create variables, initialized to 0, to hold the running totals.
num_words = 0
num_sentences = 0
num_lines = 0

# Prompt the user for the filename.
#
# No input validation is performed here, we just try to open the filename as entered.
# If this fails, the script simply terminates.
#
# We could do "in-depth" pattern checking for things like illegal characters, etc, that
# would plainly demonstrate an illegal filename, but that is not called for here, so it
# is not being done.
filename = input("Please enter the tilename to test: ")

# Now, use a try/except block to open the user-entered filename for reading.
# On open() error, print an error message and xxit.
try:
  fileHandle = open(filename, 'rt')
except:
  print ('Cannot open file %s for reading' % filename)
  sys.exit(9)

# Read the file one line at a time using the "for" loop method.
for templine in fileHandle:
    # Create a list of all the words in the line
    # All whitespace, of any length, is the split point.
    tempwords = templine.split()
    num_lines += 1
#    print (num_lines, ")", tempwords) # For test purposes only, leave in for future testing

    
    # Count the words using the length (number of elements) of the "list" created by use of
    # the ".split()" method on the templine.
    num_words += len(tempwords)

    # Assuming sentences end with ".", "?", or "!", count these characters to determine
    # the number of sentences in the file.
    num_sentences += templine.count('.')
    num_sentences += templine.count('!')
    num_sentences += templine.count('?')
    
    
fileHandle.close()

print ('-' * 50)
print ("Lines      : ", num_lines)
print ("Sentences  : ", num_sentences)
print ("Words      : ", num_words)
