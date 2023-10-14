def userInputText():
   text = input("Введите строку - ")
   return text

def vowel(text):
   text = list(text)
   ans = []
   for i in text:
       if i in 'aeiouAEIOU':
          ans.append(i)
   return str(''.join(ans))

def main():
   print(vowel(userInputText()))

if __name__ == "__main__":
   main()