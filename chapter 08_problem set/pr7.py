# Write a python function to remove a given word from a list ad strip it at the same time. 


def remove_strip(l,word):
    n=[]
    for i in l:
        if (not(i==word)):
            n.append(i.strip(word))
    return n


l=["nirmit","Sirmit","it"]

word=input('Enter word to remove and strip: ')
result=remove_strip(l,word)

print(result)