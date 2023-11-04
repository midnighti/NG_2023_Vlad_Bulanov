def convert():
    answear  = input('Enter C/c - if you want to convert to Celsius. Enter F/f - if you want to convert to Fahrenheit: ').lower()
    match answear:
        case "c":
            tempInCalsius = float(input('enter temperature in F: '))
            print(f"Temperature in Celsius is {float((tempInCalsius - 32) / 1.8)}")
        case "f":
            tempInFahrenheit = float(input('enter temperature in C: '))
            print(f"Temperature in  is {float((tempInFahrenheit * 1.8) + 32)}")
    if answear != "c" and answear != "f":
        print('I do not understand what you have written')

convert()