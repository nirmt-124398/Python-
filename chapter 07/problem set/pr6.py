# Write a program to calculate the factorial of a given number using for loop. 
no=int(input("Enter a natural number: "))
fact=1
for i in range(1,no+1):
    fact*=i
print(fact)