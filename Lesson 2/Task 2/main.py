def userInputList():
    userList = [element for element in input("Enter list - ").split()]
    return userList

def checkInt(userList):
    listOfNumbers = [element for element in userList if element.isdigit()]
    return listOfNumbers

userList = userInputList()
listOfNumbers = checkInt(userList)
print("Numbers -", listOfNumbers)
