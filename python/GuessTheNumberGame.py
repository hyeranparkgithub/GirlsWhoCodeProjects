# Guess the number game using a while loop
# Cassie and Hyeran

from random import *
#Generates a random integer.
aRandomNumber = randint(1, 10)
# For Testing: print(aRandomNumber)
guess = input("Guess a number between 1 and 10 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer
i=0
while True:
    i+=1
    if int(guess) < aRandomNumber:
        print("Guess higher!")
        guess = input("Guess a number between 1 and 10 (inclusive): ")
    elif int(guess) > aRandomNumber:
        print("Guess lower!")
        guess = input("Guess a number between 1 and 10 (inclusive): ")
    elif int(guess) == aRandomNumber:
        print("You are correct, Great Job!!!!")
    if i==2:
     break
