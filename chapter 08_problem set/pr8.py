# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(0,21):
        print(f"{n} X {i} = {n*i}")

n=int(input("Enter a natural number: "))

table(n)
