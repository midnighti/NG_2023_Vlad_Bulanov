def userInputText():
   text = input("enter str - ").lower()
   return text

def vowel(text):
   text = list(text)
   listOfLetters = []
   for element in text:
       if element in 'aeiou':
          listOfLetters.append(element)
   return set(str(''.join(listOfLetters)))

print(vowel(userInputText()))

