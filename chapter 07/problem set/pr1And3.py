# Write a program to print multiplication table of a given number using for loop.


table_of=int(input("Enter the number for its table: "))

# printing table till 10 only
for i in range(1,11):
    print(f"{table_of} * {i} = {i*table_of}")

# USING WHILE LOOP

# Attempt problem 1 using while loop.

table_of_2=int(input("Enter the number for its table: "))

i=1
while(i<11):
    print(f"{table_of_2} * {i} = {table_of_2*i}")
    i+=1


