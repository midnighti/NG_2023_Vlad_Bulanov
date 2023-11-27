def arrayOfFileLines(file):
    arrayOfFileLines = list(file.readline())
    return arrayOfFileLines

def quantity(arrayOfFileLines):
    value = len(arrayOfFileLines)
    return value

def numberOfUniqueElements(arrayOfFileLines):
    charCount = set("".join(arrayOfFileLines))

    for char in charCount:
        count = "".join(arrayOfFileLines).count(char)
        print(f"character '{char}' occurs {count} times.")

file = open(input('Enter file name: '), 'r')
lines = arrayOfFileLines(file)
print(f"quantity elements in this file is {quantity(lines)}")
numberOfUniqueElements(lines)
