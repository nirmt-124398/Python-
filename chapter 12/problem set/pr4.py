# Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError
try:
    a=int(input('enter a number: '))    
    b=int(input('enter 2nd number: '))
    print(a/b)

except Exception as e:
    print("Infinite")
