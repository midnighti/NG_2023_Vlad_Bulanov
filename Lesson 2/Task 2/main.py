def userInputList():
    lst = [a for a in input("enter list - ").split()]
    return lst

def checkInt(lst):
    nums = []
    noNums = []
    for element in lst:
        try: 
            int(element)
            nums.append(element)
        except:
            noNums.append(element)
    return nums, noNums

def main():
    lst = userInputList()
    nums, noNums = checkInt(lst)
    print("Numbers - ", nums)
    print("!numbers - ", noNums)

if __name__ == "__main__":
    main()


