def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def validfloat(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def userinputfirstnum():
    result = 0
    user_input = input("Please enter the first number: ")
    if user_input.isnumeric():
        result = int(user_input)
    elif validfloat(user_input) == True:
        result = float(user_input)
    else:
        print("Please enter a valid number.")
        userinputfirstnum()
    return result


def userinputsecondnum():
    result = 0
    user_input = input("Please enter the second number: ")
    if user_input.isnumeric():
        result = int(user_input)
    elif validfloat(user_input) == True:
        result = float(user_input)
    else:
        print("Please enter a valid number.")
        userinputsecondnum()
    return result

def user_choice():
    result = 0
    user_input = input("Would you like to add, subtract, multiply or divide? Press 1 for Add, Press 2 for Subtract, Press 3 for Multiply , Press 4 for Divide: ")
    if user_input.isnumeric:
        if int(user_input) >= 1 and int(user_input) <= 4:
            result = int(user_input)
        else:
            print("Please enter a valid number from 1 to 4.")
            user_choice()
    return result

def moreoperations():
    another = True
    user_input = input("Would you like to perform another operation? Press Y and enter for yes or N and enter to exit.")
    lowercased = user_input.lower()
    if lowercased == "y":
        another = True
    elif lowercased == "n":
        another = False
    else :
        print("Please enter Y for yes or N for no.")
        moreoperations()
    return another

def main():
    continue_operations = True
    choice = 0

    while continue_operations == True:
        choice = user_choice()
        if choice == 1:
            print("You chose add.")
            x = userinputfirstnum()
            y = userinputsecondnum()
            result = addition(x,y)
            print("The result for " + str(x) + " + " + str(y) + " is " + str(result))
            continue_operations = moreoperations()
        elif choice == 2:
            print("You chose subtract.")
            x = userinputfirstnum()
            y = userinputsecondnum()
            result = subtraction(x,y)
            print("The result for " + str(x) + " - " + str(y) + " is " + str(result))
            continue_operations = moreoperations()
        elif choice == 3:
            print("You chose multiply.")
            x = userinputfirstnum()
            y = userinputsecondnum()
            result = multiplication(x,y)
            print("The result for " + str(x) + " * " + str(y) + " is " + str(result))
            continue_operations = moreoperations()
        elif choice == 4:
            print("You chose divide.")
            x = userinputfirstnum()
            y = userinputsecondnum()
            result = division(x,y)
            print("The result for " + str(x) + " / " + str(y) + " is " + str(result))
            continue_operations = moreoperations()

            
main()
