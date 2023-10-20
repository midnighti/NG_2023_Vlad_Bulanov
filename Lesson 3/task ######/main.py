import string

encodedMessage = 'r186022q0931nsr9sr0690857r32s85r50165r7sor0966q49609rs1981s920p6'

def decodeMessage(encoded_message):
    alphabet = string.ascii_lowercase
    decodedMessage = ''
    for char in encodedMessage:
        if char in alphabet:
            decodedChar = alphabet[(alphabet.index(char) + 13) % 26]
            decodedMessage += decodedChar
        else:
            decodedMessage += char
    return decodedMessage

def main():
    print(decodeMessage(encodedMessage))

if __name__ == "__main__":
    main()

