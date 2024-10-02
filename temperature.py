unit = input("f: Fahrenheit\tc : Celsius\tk: Kelvin \nEnter unit: ")
temp = float(input("Enter temperature: "))

if unit.lower() == "f":
    if temp >212:
        print("Boiling...")
    else:
        print("Not boiled yet...")
elif unit.lower() =="c":
    if temp >100:
        print("Boiling...")
    else:
        print("Not boiled yet...")
elif unit.lower() =="k":
    if temp >313:
        print("Boiling...")
    else:
        print("Not boiled yet...")
else:
    print("invalid unit")