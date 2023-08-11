import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


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
    print("8. Sin")
    print("8. Cos")
    print("9. Tan")

    print("")
    print("--------------------------------------------------------------------")
    print("")

    operator = input("Enter Number of Operation (1/2/3/4/5/6/7/8/9) : ")

    if operator in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if operator in('1', '2'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))

        elif operator in ('3'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter the Number that want to Multiplied : "))

        elif operator in ('4'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Eenter the Number that want to Divide : "))

        elif operator in ('5'):
            num1 = float(input("Enter the Number that want to get Square Root : "))

        elif operator in ('6'):
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Eenter the number Power Value : "))

        elif operator in ('7'):
            num1 = float(input("Number that want to get Sin : "))

        elif operator in ('8'):
            num1 = float(input("Number that want to get Cos : "))

        elif operator in ('9'):
            num1 = float(input("Number that want to get Tan : "))
        

        if operator == '1':
            print("Total is : ", add(num1, num2))
        
        elif operator == '2':
            print("Subtraction is : ", sub(num1, num2))

        elif operator == '3':
            print("Multiplication is : ", multiply(num1, num2))

        elif operator == '4':
            print("Division is : ", divide(num1, num2))  

        elif operator == '5':
            print("Square Root is : ", squreRoot(num1))

        elif operator == '6':
            print("Power Value is : ", powerV(num1, num2))

        elif operator == '7':
            print("Sin Value is : ", SinV(num1))

        elif operator == '8':
            print("Cos Value is : ", CosV(num1))

        elif operator == '9':
            print("Tan Value is : ", TanV(num1))

    else:
        print("You Enterd Operation is Invalid Operation")


if __name__ == "__main__":
    main_cal()