# Determine whether num is even or not
from random import *

while True:
    aRandomNumber = randint(1,20)
    start=input("Type START to begin. ")
    if start=="start":
        print(aRandomNumber)

        if aRandomNumber % 2 == 0:
            print("even")
        else:
            print("odd")
