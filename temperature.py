symbol = input("Enter the symbol (C/F/K/L): ")
temp = float(input("Enter the temperature: "))

if symbol == "C":
    temp = (temp * 9 / 5) + 32
    print(f"By converting Celsius to Fahrenhit: {round(temp ,2 )}F")
elif symbol == "F":
    temp = (temp - 32) * 5 / 9
    print(f"By converting Fahrenhit to Celsius: {round(temp ,2 )}C")
elif symbol == "L":
    temp = temp + 273.15
    print(f"By converting Celsius to Kelvin: {round(temp ,2 )}K ")
elif symbol == "K":
    temp = temp - 273.15
    print(f"By converting Kelvin to Celsius: {round(temp ,2 )}C")
else:
    print("Enter a valid symbol")