try:
    a=int(input('Enter a valid number: '))
    print(a)

except Exception as e:
    print(e)

else : # control goes to esle only if try is succefull
    print("Hi, I am inside else")
