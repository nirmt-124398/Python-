# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("poems.txt") as f:
    list=f.readline()
    if(("twinkle" in list) or ("Twinkle" in list)):
        print("twinkle exists in file")
    else:
        print("twinkle doesn't exists in file")
