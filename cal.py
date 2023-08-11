import math

def main_cal():
    print("")
    print("--------------------------------------------------------------------")
    print("--------------------- Scientific Calculator ------------------------")
    print("--------------------------------------------------------------------")
    print("")
    print("Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("")
    print("--------------------------------------------------------------------")
    print("")

    operator = input("Enter Number of Operation (1/2/3/4/5/6) : ")

    if operator in ('1', '2', '3', '4', '5', '6'):
        if operator in('1', '2'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))

        elif operator in ('3'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter the Number that want to Multiplied : "))

        elif operator in ('4'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Eenter the number that want to Divide : "))

        elif operator in ('5'):
            num1 = float(input("Enter the Number that want to get Square Root : "))
    else:
        print("You Enterd Operation is Invalid Operation")


if __name__ == "__main__":
    main_cal()