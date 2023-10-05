def userInput(text):
    return input(text)

def concertToC(f):
    print(int((f - 32) / 1.8))

def cinvertToF(c):
    print(int((c * 1.8) + 32))

def calc(answear):
    if answear == "c" or answear == "C":
        print(convertToC(int(userInput('Vvedite temperatyry v F'))))
    if answear == "f" or answear == "F":
        print(convertToF(int(userInput('Vvedite temperatyry v C'))))


def calcMode(text):
    return userInput(text)

def main():
    print(calc(calcMode('Введи С/с - если хочешь перевести в градусы Цельсия/nВведи F/f - если хочешь перевести в градусы Фаренгейта')))

if __name__ == "__main__":
    main()