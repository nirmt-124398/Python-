from random import randint

n=randint(1,100)
guases=0
answer=0
while(answer != n):
    answer=int(input("Enter a number: "))

    if(answer>n):
        print("LOWER!")
    else:
        print("GREATER!")
    guases+=1

print(f"You predicted {answer} in {guases} try's")


