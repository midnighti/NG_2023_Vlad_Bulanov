import json

def userInputKey():
    key = input("enter key name: ")
    return key

json_data = '''
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
'''

data = json.loads(json_data)

def valueByKey(data, key):
    if key in data:
        return data[key]
    for key, value in data.items():
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
        print(f"Key '{key}' is !found JSON.")

if __name__ == "__main__":
    main()