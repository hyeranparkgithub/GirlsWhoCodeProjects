# Chatbot

# --- Define your functions below! ---
def intro():
    print("Hello!")

def processInput(answer):
    if answer == "hi":
        sayGreeting()
    else:
        sayDefault()
def sayDefault():
    print("That's cool!")

def sayGreeting():
    print("How are you? ")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        processInput(answer)




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
