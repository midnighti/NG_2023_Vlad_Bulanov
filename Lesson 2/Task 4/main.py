def userInputText():
   text = input("enter str - ")
   return text

def vowel(text):
   text = list(text)
   listOfLetters = []
   for element in text:
       if element in 'aeiouAEIOU':
          listOfLetters.append(element)
   return set(str(''.join(listOfLetters)))

def main():
   print(vowel(userInputText()))

if __name__ == "__main__":
   main()
