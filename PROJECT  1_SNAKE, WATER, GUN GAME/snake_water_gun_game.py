import random

print('''
1 for snake(s)
-1 for water(w)
0 for gun(g)

''')

computer=random.choice([-1,0,1])
youstr=input("Enter your Choice: ").lower()
youdict={
    "s":1,
    "w":-1,
    "g":0,
}
reversedict={
     1:"Snake",
     -1:"Water",
     0:"Gun",
}
# Validate user input
if youstr not in youdict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:

    you=youdict[youstr]

    print(f"Computer's choice is {reversedict[computer]} \nYour choice is {reversedict[you]}")



    if(computer==you):
        print("It's a DRAW")
    else:
        #This one is less complex and good for readability
        if(computer==-1 and you==1):
            print("You win!")
        elif(computer==-1 and you==0):
            print("You lose!")
        elif(computer==1 and you==-1):
            print("You lose!")
        elif(computer==1 and you==0):
            print("You win!")
        elif(computer==0 and you==-1):
            print("You win!")
        elif(computer==0 and you==1):
            print("You lose!")

    #     OR --- This one takes less execution time.

    
    #     if(computer==you):
    #       print("It's a DRAW")
    #     else:
    #       if(computer==-1 and you==1) or (computer==1 and you==0) or(computer==0 and you==-1):
    #         print("You win!")
    #       else:
    #         print("You lose!")


     
        