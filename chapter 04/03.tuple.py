# Syntax of tuple--It is unmutable

a=() #empty
b=(1,) #single value 
c= (12,34,56)
print(c[1])

# METHODS ON TUPLE'S
t = (1, 2, 3, 1, 4, 1)


#1
new= t.__add__(c)
print(new)

#2
new_t=t.__contains__(3)
print(new_t)
new_t=t.__contains__(9)
print(new_t)

#3
new_t=new.count(1)
print(new_t)

#4
new_t=new.index(12)
print(new_t)
new_t=new.index(1)
print(new_t)

#5
new_t=len(new)
print(new_t)

#6 tuple unpacking   
info=("Nirmit",20,"Rampal")
first_name,age,last_name=info

print(first_name)
print(last_name)
print(age)

#7 membership test------ True/False

print(20 in info) #true
print(21 in info) #false