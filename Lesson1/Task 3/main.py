def userInput(text):
    return input(text)

def convertToC(f):
    print(f"Temperature in Celsius is {int((f - 32) / 1.8)}")

def convertToF(c):
    print(f"Temperature in Fahrenheit is {int((c * 1.8) + 32)}")

def calc():
    answear = userInput('Enter S/s - if you want to convert to Celsius. Enter F/f - if you want to convert to Fahrenheit: ') 
    if answear == "c" or answear == "C":
        print(convertToC(int(userInput('enter temperature in F: '))))
    if answear == "f" or answear == "F":
        print(convertToF(int(userInput('enter temperature in C: '))))

def main():
    print(calc())

if __name__ == "__main__":
    main()
