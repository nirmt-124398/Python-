#variable type hint
age:int=4
#FUNCTION type hint
print(age.is_integer())

def sum(a:int,b:int)->int:
    return a+b

s:int=sum(5,4)#While writing arg tel programmer what is Output of this fun and type of arg.. accept by fuc
print(s)
