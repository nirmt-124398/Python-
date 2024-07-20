#  Write a program to find the sum of first n natural numbers using while loop.

no=int(input("Enter a natural number: "))
sum=0
i=1
while(i<=no):
    sum+=i
    i+=1
else:
    print(sum)