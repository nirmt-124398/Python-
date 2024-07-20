a=int(input("Enter marks: "))
b=int(input("Enter marks: "))
c=int(input("Enter marks: "))


total_percent=((a+b+c)/300)*100
if(total_percent>=40 and a>=33 and b>=33 and c>=33):
    print("Congrates,You passed",total_percent)
else:
    print("Congrates,You FAILED in life",total_percent)
    