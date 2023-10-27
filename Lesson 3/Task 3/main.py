import json

def userInputFileName():
    return input("Enter file name: ")

def userInputKey():
    key = input("Enter key name: ")
    return key

def openJsonData(fileName):
    with open(fileName, 'r') as file:
        jsonData = json.load(file)  # Use json.load to read the entire JSON file
    return jsonData

data = openJsonData(userInputFileName())

def valueByKey(data, key):
    if key in data:
        return data[key]
    for nested_key, value in data.items():  # Changed 'key' to 'nested_key'
        if isinstance(value, dict):
            result = valueByKey(value, key)
            if result is not None:
                return result

def main():
    key = userInputKey()
    value = valueByKey(data, key)
    if value is not None:
        print(f"{key} : {value}")
    else:
        print(f"Key '{key}' is not found in the JSON.")

if __name__ == "__main__":
    main()
