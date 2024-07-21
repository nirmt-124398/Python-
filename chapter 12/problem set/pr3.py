# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number.
n=int(input('enter a number: '))
list=[f"{n} X {i} = {n*i}" for i in range(1,11)]
print(list)