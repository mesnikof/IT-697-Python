"""This is the solution script for the IT-647 Week 4 assignment - Michael Mesnikoff """

# Import the 'math' library.
import math

# 1) First, just print the numbers 1 thru 5, one per line.
print("Show the integers 1 through 5 (inclusive) using a \"for\" loop:")
for n in range(6):
    if(n > 0) and (n < 6):
        print(n)


# 2) Now, print the sum of two static integers.
print("\nThe sum of 3 + 4 is:")
print(3 + 4)


# 3) Now, print the sum of pi plus the sqare root of 2.
print("\nThe sum of pi and the sqare root of two is:")
print(math.pi + (math.sqrt(2)))


# 4) Now, print the sum of cosine-30 and sine-30.
print("\nThe sum of cos30 and sin30 is:")
print((math.cos((30 * (math.pi/180)))) + (math.sin((30 * (math.pi/180)))))


# 5) Now, take uer input of three integers and print them using formatted output.
# Left-justification, six columns wide.
# Note: No input validation here.
x, y, z = input("\nEnter three integers, separated by spaces: ").split()
print("\nFirst Integer: %6d, Second Integer: %6d, Third Integer: %6d" % (int(x), int(y), int(z)))


# 6) Next, get the user input for the radius of a circle, output the area.
# Note: no input validation here.
r = float(input("\nInput the desired radius circle: "))
print("The area of the circle is: ", (math.pi * 2) * r)


# 7) Now, get to numbers from the user, output the greater of the two.
# Note: still no input validation being performed.
x, y = input("\nInput two numbers, separated by a space: ").split()
x = float(x)
y = float(y)
if (x > y):
    print("The greater number is: ", x)
elif (y > x):
    print("The greater number is: ", y)
else:
    print("The numbers are equal.")


# 8) Now, take user input of two booleans.  Then print the negation of
# performing an AND operation on the two values.
# The funcion is used to allow multiple iterations of the input action.
# Note: Still very little imput validation here.
def t_or_f():
    tf = 99
    while(tf == 99):
        tf = input("Input \"t\" or \"f\" (true or false):")
        if ((tf == 't') or (tf == 'T')):
            tf = 1
        elif ((tf == 'f') or (tf == 'F')):
            tf = 0
        else:
            print("Only \"t\" or \"f\".  Please try again.")
            tf = 99
    return(tf)

print("\nInput two boolean values, one at a time.")
val1 = t_or_f()
val2 = t_or_f()
if (val1 and val2):
    print("The negation of", val1, "AND", val2, "is FALSE.")
else:
    print("The negation of", val1, "AND", val2, "is TRUE.")


# 9, 10) Create a reuseable function to prevent entering 0 as an integer.
def not_zero(count):
    x = 0
    while(x == 0):
        x = int(input("%d) Enter an integer: " % (count)))
        if (x == 0):
            print("Input cannot be 0. Please try again.")
    return(x)

        
# 9) Next, prompt the user for ten non-zero integers using a 'for' loop,
# and print out their sum.
# Note: Still very little imput validation here.
print("\nInput 10 integers, one at a time, when prompted, to generate a sum.")
sum_total = 0
for count in range(10):
    sum_total = sum_total + not_zero(count + 1)
print("The sum of the entered integers is: ", sum_total)


# 10) Finally, prompt the user for ten non-zero integers using a 'while' loop,
# and print out their sum.
# Note: Still very little imput validation here.
print("\nInput 10 integers, one at a time, when prompted, to generate a sum.")
sum_total = 0
count = 1
while(count <= 10):
    sum_total = sum_total + not_zero(count)
    count += 1
print("The sum of the entered integers is: ", sum_total)
