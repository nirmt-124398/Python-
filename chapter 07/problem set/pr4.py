# Write a program to find whether a given number is prime or not. 

no=int(input("Enter a prime number: "))

for i in range(2,no):
    if(no%i==0):
        print("No. is not prime")
        break
else:
    print("number is prime")

 