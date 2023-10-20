rdef userInput(text):
    return input(text)

def convertToC(f):
    print(int((f - 32) / 1.8))

def convertToF(c):
    print(int((c * 1.8) + 32))

def calc(answear):
    if answear == "c" or answear == "C":
        print(convertToC(int(userInput('enter temperature in F'))))
    if answear == "f" or answear == "F":
        print(convertToF(int(userInput('enter temperature in C'))))


def calcMode(text):
    return userInput(text)

def main():
    print(calc(calcMode('Enter S/s - if you want to convert to Celsius/nEnter F/f - if you want to convert to Fahrenheit')))

if __name__ == "__main__":
    main()
