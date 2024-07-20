list=[20,23,24,25,26,27,28]

for i in list:
    print(i)

t= (1,2,3,4,5,6)

for i in t:
    print(i)

str="NirmIT"

for i in str:
    print(i)



# We can also specify the start, stop and step-size as follows:
times=0
for i in range(0,81,4):
    print(f"4 * {times} = {i}")
    times +=1


# For loop with else

l=[10,20,30,40]

for i in l:
    print(i)
else:
    print("DONE")

# VS

for i in l:
    print(i)
    break
else:
    print("DONE")

#     The else block is executed when the for loop completes normally (i.e., it iterates over all items in the list without encountering a break        statement).
# If the loop is terminated by a break statement, the else block will not be executed


# ‘continue’ is used to stop the current iteration of the loop and continue with the next 
# one. It instructs the Program to “skip this iteration”. 

for i in range(0,4):
    if(i==2):
        continue
    print(i)


for i in range(654):
    pass                    # Will work o it later on
i=0
while(i<10):
    print(i)
    i+=1