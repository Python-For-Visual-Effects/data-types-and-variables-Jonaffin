"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32


# 2.- Do the same as the question one but this time use variables instead of 
# numbers.

# 3.- Make a program that prints a sentence that includes at least 3 variables.

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"

print("1.")
def addition(number1, number2):
    answer = 64 + 32
    return answer

print(addition(2,3))

print("2.")
number64 = 64
number32 = 32
print (number64 + number32)

print("3.")
subject = "Python"
college = "Seneca College"
student = "Jonathan Balazs"
nickname = "Jonaffin"

print(
    "Hi, I am " + student + " and I am a " + subject + " student at " + college + ". " "My nickname on Github is " + nickname + "."
)

print("4.")
q4subject = "This is my first Python program. "
print("I've assigned this string as: " + str(q4subject))
print(len("This is my first Python program."))

print("5.")
hnum = (1920 * 0.1 + 1920)
vnum = (1080 * 0.1 + 1080)
print(
    "The 10% overscan of 1920 is " + str(hnum), "and the 1080 is " + str(vnum)
    )
