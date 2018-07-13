# Calculate the sum of each item in list
def intro():
    print("Welcome to the list of numbers calculator!")

def length():
    num = int(input("How many numbers (length) :"))
    first = []
    for n in range(num):
        numbers = int(input("Enter number :"))
        first.append(numbers)
    print("sum of elements in given list is :", sum(first))

def main():
    intro()
    length()





if __name__ == "__main__":
    main()
