try:
    a=int(input('Enter a valid number: '))
    print(a)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
