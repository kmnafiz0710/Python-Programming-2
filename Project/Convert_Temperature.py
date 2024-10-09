#Celsius to Fahrenheit and Kelvin
#Here I tried to create a system to convert temperature among Celsius, Fahrenheit and Kelvin.

def c_to_others(c_temp):
    fahrenheit = (c_temp * 9/5) + 32
    kelvin = c_temp + 273.15
    return fahrenheit, kelvin

#Fahrenheit to Celsius and Kelvin
def f_to_others(f_temp):
    celsius = (f_temp - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

#Kelvin to Celsius and Fahrenheit
def k_to_others(k_temp):
    celsius = k_temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

UserInput = input("Which temperature unit do you want to input?\n (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()


if UserInput == 'C':
    c_input = float(input("Enter temperature in Celsius: "))
    fahrenheit, kelvin = c_to_others(c_input)
    print(f"{c_input} °Celsius is equal to {fahrenheit} °Fahrenheit and {kelvin} Kelvin")

elif UserInput == 'F':
    f_input = float(input("Enter temperature in Fahrenheit: "))
    celsius, kelvin = f_to_others(f_input)
    print(f"{f_input} °Fahrenheit is equal to {celsius} °Celsius and {kelvin} Kelvin")

elif UserInput == 'K':
    k_input = float(input("Enter temperature in Kelvin: "))
    celsius, fahrenheit = k_to_others(k_input)
    print(f"{k_input} Kelvin is equal to {celsius} °Celsius and {fahrenheit} °Fahrenheit")

else:
    print("Invalid input! Please enter C, F, or K.")

