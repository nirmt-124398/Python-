# Write a program to print multiplication table of n using for loops in reversed order.

n=int(input("Enter a natural number: "))
for i in range(10,0,-1): 
    print(f"{n} X {i} = {n*i}")