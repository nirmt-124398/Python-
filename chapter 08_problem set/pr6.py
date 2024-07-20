# Write a python function which converts inches to cms.

def inchTocm(inches):
    cm=inches*2.54
    print(f"Centimeters: {cm}")

n=int(input("Enter Inches: "))
inchTocm(n)
