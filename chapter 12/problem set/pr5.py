# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n=int(input('enter a number: '))
list=[f"{n} X {i} = {n*i} \n" for i in range(1,11)]



with open("Tables.txt","a") as f:
        f.writelines(list)
