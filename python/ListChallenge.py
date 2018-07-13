#imports the ability to get a random number
from random import *

print("Welcome to the Name Generator!")
#Create the list of names (Boys)
BoyList = ["Sam", "Zack", "Justin", "Devon", "Elyon", "Jinho",
 "Cole", "jikobe", "David", "Suga", "Tyler", "Matt", "John", "Jun", "Luke",
 "Andrew", "Ethan", "Jordan", "Ashton", "Keen", "Kirsten"]

#Create the list of names (Girls)
GirlList = ["Sharkisha", "Beck", "Anna", "Elsa", "Allison", "Eunice",
 "Cheetah", "Shithe", "Elyona", "Evangela", "Ciel", "Ivan", "Ivy", "Beyonce",
 "Squash", "Angela", "Sarah", "Hannah", "Lucy", "Lily", "Danielle"]

#Generates a random integer.
GirlRandomIndex = randint(0, len(GirlList)-1)
BoyRandomIndex = randint(0, len(BoyList)-1)

girlOrBoy = input("Do you want a GIRL or BOY name? ")

while True:
    if girlOrBoy == "girl":
        start = input("Type START to generate a name. ")
    if start == "start":
                print(GirlList[GirlRandomIndex])

    elif girlOrBoy == "boy":
        start = input("Type START to generate a name. ")
    if start == "start":
                print(BoyList[BoyRandomIndex])
