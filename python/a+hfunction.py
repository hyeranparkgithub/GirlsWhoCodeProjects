#Multiply #s In List
def intro():
    print("Welcome to the Multiplication Calculation Application!!")

def calc():
    num = int(input("How many numbers would you like to calculate? : "))
    mult = []
    for n in range(num):
        numbers = int(input("Enter number : "))
        mult.append(numbers)
    print("product of elements in givn list is ", multiply(mult))

def multiply(mult):
    product = 1
    for num in mult:
        product *= num
    return product

def main():
    intro()
    calc()




if __name__ == "__main__":
    main()
