list=[4,6,2,5,9]

sqlist=[]
for i in list:
    sqlist.append((i+4)*(i-4))
print(sqlist)

# OR

sqlist=[((i+4)*(i-4)) for i in list]
print(sqlist)