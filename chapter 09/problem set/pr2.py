# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score. 

import random

def game():
    print("You are playing the game...")
    score=random.randint(1,10)
    #Fetch hiscore
    with open("Hi-score.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    if(score>hiscore):
        #write scoret to file 
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    print(f"Your score: {score}")


game()