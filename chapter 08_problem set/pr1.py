# Write a program using functions to find greatest of three numbers. 
def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greatest number.")
    elif(b>a and b>c):
        print("b is greatest number.")
    elif(c>b and c>a):
        print("c is greatest number.")

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

greatest(a,b,c)