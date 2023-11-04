import math
import gmpy2


def userInputNum():
    value = int(input("enter number - "))
    return value

def userInputCalcMode():
    mode = input("choose aperation: +, -, *, /, sqrt, degree - ")
    return mode


def add(valueA, valueB):
    return print(valueA + valueB)

def subtract(valueA, valueB):
    return print(valueA - valueB)

def multiply(valueA, valueB):
    return print(valueA * valueB)

def devide(valueA, valueB):
    return print(valueA / valueB)

def sqrt(valueA, valueB):
    return print(gmpy2.root(valueA, valueB))

def degree(valueA, valueB):
    return print(pow(valueA, valueB))


def operation(valueA, valueB, mode):
    match mode:
        case "+":
            return add(valueA, valueB)
        case "-":
            return subtract(valueA, valueB)
        case "*":
            return multiply(valueA, valueB)
        case "/":
            return devide(valueA, valueB)
        case "sqrt":
            return sqrt(valueA, valueB)
        case "degree":
            return degree(valueA, valueB)
        

def main():
    operation(userInputNum(), userInputNum(), userInputCalcMode())


if __name__ == "__main__":
    main()
