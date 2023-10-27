def userInputFileName():
    return input('Enter file name: ')

def openFile(fileName):
    return open(fileName, 'r')

def arrayOfFileLines(file):
    arrayOfFileLines = list(file.readline())
    return arrayOfFileLines

def quantity(arrayOfFileLines):
    value = len(arrayOfFileLines)
    return value

def numberOfUniqueElements(arrayOfFileLines):
    charCount = {}

    for line in arrayOfFileLines: 
        for char in line:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1

    for char, count in charCount.items():
        print(f"character '{char}' occurs {count} times.")

def main():
    fileName = userInputFileName()
    file = openFile(fileName)
    lines = arrayOfFileLines(file)
    print(f"quantity elements in this file is {quantity(lines)}")
    numberOfUniqueElements(lines)

if __name__ == "__main__":
    main()
