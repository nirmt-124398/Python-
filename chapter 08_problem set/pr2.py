# Write a python program using function to convert Celsius to Fahrenheit.

def CelsiusToFahrenheity(celsius):
    f=celsius*(9/5)+32
    return f

CelTmp=float(input("Give temperature in celsius: "))

display=CelsiusToFahrenheity(CelTmp)
print(f"Temperature in Fahrenheit: {display}")