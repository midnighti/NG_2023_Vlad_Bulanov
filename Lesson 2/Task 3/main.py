from prettytable import PrettyTable

def userInputNum():
    num = int(input("Введите число - "))
    return num

def listOfNums(num):
    lst = []
    for element in range(num + 1):
        if element == 0:
            continue
        lst.append(element[num] - element)
    return lst 

def divide():
    lst1, lst2 = listOfNums()
    dividedList = []
    for element1 in range(len(lst1)):
        for element2 in range(len(lst2)):
            if lst1[element1] % element2 == 0:
                dividedList.append(lst1[element1])
            else:
                continue
    return dividedList

def isPrime(lst):
    if lst % lst == 0 and lst != 0:
        return print("Prime")
    else:
        return print("No prime")

def createTable():
    th = ["nums", "divedeNums", "primeNums"]
    td = [listOfNums(userInputNum()), divide(), isPrime(listOfNums())]
    columns = len(th)
    table = PrettyTable(th)
    while td:
        table.add_row(td[:columns])
        td = td[columns:]

print(createTable())