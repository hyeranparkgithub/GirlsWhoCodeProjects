
import json

questions = ["What is your name? ",
"What is your date of birth (MM,DD,YYYY)? ",
"What is your age? ",
"Where do you call home (City, State, Country)? ",
"Would you like to start over (yes or no)? "]

totalResponse = []


def intro():
    print("Hello, thank you for taking your time to answer the Broski Survey!")

def name(responses):
    name = input(questions[0])
    print("Nice to meet you,", name + ".")
    responses["name"] = name

def birthday(responses):
    birth = input(questions[1])
    print("Oh cool!")
    responses["birthday"] = birth

def age(responses):
    age = input(questions[2])
    print("Wow you still have a long way to go...")
    responses["age"] = age

def home(responses):
    home = input(questions[3])
    print("Alright, sounds good.")
    responses["home"] = home


def newSurvey(responses):
    totalResponse.append(responses)

    again = input(questions[4])
    if again == "no":
        print(totalResponse)
        print("Thank you for your time.")

    elif again == "yes":
        main()


def main():
    responses = {}
    intro()
    name(responses)
    birthday(responses)
    age(responses)
    home(responses)
    newSurvey(responses)





if __name__ == "__main__":
  main()
