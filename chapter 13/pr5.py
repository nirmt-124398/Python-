# 5. Write a program to find the maximum of the numbers in a list using the reduce 
# function.
from functools import reduce
list=[1,2,54,67,222]

greater=lambda a,b:a if (a>b) else b

maxlist=reduce(greater,list)
print(maxlist)