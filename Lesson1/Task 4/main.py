import math


def userInputNum():
    a = int(input("enter number - "))
    return a

def userInputCalcMode():
    mode = input("choose aperation: +, -, *, /, sqrt, degree - ")
    return mode


def add(a, b):
    return print(a + b)

def subtract(a, b):
    return print(a - b)

def multiply(a, b):
    return print(a * b)

def devide(a, b):
    return print(a / b)

def sqrt(a, b):
    return print(math.sqrt(a), math.sqrt(b))

def degree(a, b):
    return print(pow(a, b))


def operation(a, b, mode):
    match mode:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return devide(a, b)
        case "sqrt":
            return sqrt(a, b)
        case "degree":
            return degree(a, b)
        

def main():
    operation(userInputNum(), userInputNum(), userInputCalcMode())


if __name__ == "__main__":
    main()
