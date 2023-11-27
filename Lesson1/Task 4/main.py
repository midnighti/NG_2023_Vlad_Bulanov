import math
import gmpy2


def userInputNum():
    value = int(input("enter number - "))
    return value

def userInputCalcMode():
    mode = input("choose aperation: +, -, *, /, sqrt, degree - ")
    return mode

def operation(valueA, valueB, mode):
    match mode:
        case "+":
            return print(valueA + valueB)
        case "-":
            return print(valueA - valueB)
        case "*":
            return print(valueA * valueB)
        case "/":
            return print(valueA / valueB)
        case "sqrt":
            return print(gmpy2.root(valueA, valueB))
        case "degree":
            return print(pow(valueA, valueB))
        
operation(userInputNum(), userInputNum(), userInputCalcMode())

