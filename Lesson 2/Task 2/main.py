def userInputList():
    userList = [element for element in input("enter list - ").split()]
    return userList

def checkInt(userList):
    listOfNumbers = []
    listOfLetters = []
    for element in userList:
        try: 
            int(element)
            listOfNumbers.append(element)
        except:
            listOfLetters.append(element)
    return listOfNumbers, listOfLetters

def main():
    userList = userInputList()
    listOfNumbers, listOfLetters = checkInt(userList)
    print("Numbers - ", listOfNumbers)
    print("!numbers - ", listOfLetters)

if __name__ == "__main__":
    main()


