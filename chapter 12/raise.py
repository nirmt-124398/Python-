a=int(input('Enter a number: '))


if((b:=int(input('Enter a 2nd number: ')))==0):
    raise ZeroDivisionError("Division with 0 not possible.")
else:
    print(f"Division: {a/b}")