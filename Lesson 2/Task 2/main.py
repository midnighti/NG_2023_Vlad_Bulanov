def userInputList():
    userList = [element for element in input("Enter list - ").split()]
    return userList

def checkInt(userList):
    listOfNumbers = [element for element in userList if element.isdigit()]
    return listOfNumbers

listOfNumbers = checkInt(userInputList())
print("Numbers -", listOfNumbers)
