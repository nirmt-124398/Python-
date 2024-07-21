# 4. Write a program to filter a list of numbers which are divisible by 5.

list1=[1,5,23,25,75,32,55]

fivedivi=lambda a:a if a%5==0 else None

filteredlist=list(filter(fivedivi,list1))

print(filteredlist)