def openFile():
    return open('text.txt' , 'r')

def arrayOfFileLines(file):
    arr = list(file.readline())
    return arr

# print(arrayOfFileLines(openFile()))

def quantity(arr):
    value = len(arr)
    return value

def numberOfUniqueElements(arr):
    charCount = {}

    for char in arr:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    for char, count in charCount.items():
        print(f"character '{char}' occurs {count} times.")

def main():
    print(f"quantity elements in this file is {quantity(arrayOfFileLines(openFile()))}")
    numberOfUniqueElements(arrayOfFileLines(openFile()))

if __name__ == "__main__":
    main()