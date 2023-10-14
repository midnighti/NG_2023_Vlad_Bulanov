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
    stop = 2
    i = 0
    cell = len(th)
    for cell in td:
        print("<td>%s</td>\n" % cell)
        if i == stop: 
            print ("</tr><tr>\n")
            stop == i + 3
        i += 1
def main():
    print(createTable())

if __name__ == "__main__":
    main()