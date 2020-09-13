# INPUT smaller bound of range
# INPUT larger bound of range
# Declare maxGuesses for computer
# Declare guess as smaller + larger / 2
# WhILE count is not equal to maxGuesses
#   guess = smaller + larger / 2
#   PRINT "Your number is" guess
#   INPUT userResponse
#   IF userResponse == ">", THEN smaller = giess + 1
#   ELSEIF useresponse == "<", THEN larger = guess - 1
#   ELSEIF userResponse == "=", THEN PRINT "Hooray, I've got it in", count, "tries!"
#   BREAK
# ELSE, PRINT "I'm out of guesses, and you cheated!"
# END.

import math
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxGuesses = round(math.log(larger - smaller + 1, 2))
count = 0
guess = int((smaller + larger) / 2)
while count != maxGuesses:
    count += 1
    guess = int((smaller + larger) / 2)
    print(smaller, larger)
    print("Your number is ", guess)
    userResponse = input("Enter =, <, or >: ")
    if userResponse == '>':
        smaller = guess + 1
    elif userResponse == '<':
        larger = guess - 1
    elif userResponse == '=':
        print("Hooray, I've got it in", count, "tries!")
        break
else:
    print("I'm out of guesses, and you cheated")
