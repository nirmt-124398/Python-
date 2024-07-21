#without walcrus operator
list=[1,2,3,4,5]
n=len(list)

if(n>3):
    print("This is withou Walcrus operator.")
#with Walcrus operator
if(n:=len([1,2,3,4,5]))<7:
    print("This is done with walcrus operator")