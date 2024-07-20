# Write a program to print the following star pattern. 
# * * * 
# *    *    for n = 3 
# * * *

n=int(input("Enter a natural number: "))
for i in range(1,n+1):
    if(i%2==0):
        print("*  *")
    else:
        print("***")

# but question also translates to 1st and last should be *** and rest *  * For that this solution.
print("\n 2nd way \n")

for i in range(1,n+1):
    if(i==1 and i==n):
        print("***")
    else:
        print("*  *")