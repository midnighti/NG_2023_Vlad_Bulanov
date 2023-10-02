def userInput(text):
    return int(input(text))

def sum(a, b):
    return a + b

def main():
    print(sum(userInput('Vvedi 1 4islo '), userInput('Vvedi 2 4islo ')))

if __name__ == "__main__":
    main()