from termcolor import colored


def main():
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y
    
    
    print(colored("+-------------------+", 'red'))
    print(colored("+----Calculator-----+", 'red'))
    print(colored("+-------------------+", 'red'))
    print(colored("===================================\n", 'green'))
    
    print("Select operation.")
    print("1 FOR ADDITION")
    print("2 FOR SUBTRACTION")
    print("3 FOR MULTIPLICATION")
    print("4 FOR DIVISION")
    
    while True:
        # Take input from the user
        choice = input("Enter the operation you need: ")
    
        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter Your First Number: "))
            num2 = float(input("Enter Your Second Number: "))
    
            if choice == '1':
                print(add(num1, num2))
    
            elif choice == '2':
                print(subtract(num1, num2))
    
            elif choice == '3':
                print(multiply(num1, num2))
    
            elif choice == '4':
                print(divide(num1, num2))
            break
        else:
            print("Invalid Input")

    rerun = input("Do You Want To Continue Y/n: ")

    if rerun in ('y', 'yes' 'Y', 'Yes', 'YES', 'NO', 'n', 'N' 'No', 'no'):

        if rerun == 'Y':
            main()
        elif rerun == 'y':
            main()
        elif rerun == 'yes':
            main()
        elif rerun == 'Yes':
            main()
        elif rerun == 'YES':
            main()
        elif rerun == 'n':
            print("Bye....")
        elif rerun == 'NO':
            print("Bye....")
        elif rerun == 'N':
            print("Bye....")
        elif rerun == 'No':
            print("Bye....")
        elif rerun == 'no':
            print("Bye....")


main()

