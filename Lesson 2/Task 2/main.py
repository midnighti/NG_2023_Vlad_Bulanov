def userInputList():
    userList = [element for element in input("enter list - ").split()]
    return userList

def checkInt(userList):
    listOfNumbers = []
    for element in userList:
        try: 
            int(element)
            listOfNumbers.append(element)
        except:
            continue
    return listOfNumbers

def main():
    userList = userInputList()
    listOfNumbers = checkInt(userList)
    print("Numbers - ", listOfNumbers)

if __name__ == "__main__":
    main()


