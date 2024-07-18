# Set is a collection of non-repetitive elements.

s={1,2,3,45}
e= set()# empty set
print(e)


#Methods
#1 add
s.add(99)
print(s)


#2 remove,discard and pop

s1={1,2,3,4,56,6}
print(s1)
s1.remove(2)
print(s1)

s1.discard(4)
print(s1)

print(s1.pop())

#3 set operationn
set1={1,2,3,4}
set2={2,3,4,5}

#3.1 Union
set3=set1.union(set2)
print(set3)             #{1, 2, 3, 4, 5}

#3.2 Intersection
set3=set1.intersection(set2)
print(set3)             #{2, 3, 4}

#3.3 Difference ---Returns a new set with elements in the set that are not in other_set

set3=set1.difference(set2)
print(set3)             #{1}

#3.4 symmetric difference ---Returns a new set with elements in either the set or other_set but not in both.

set3=set1.symmetric_difference(set2)
print(set3)             #{2, 3, 4}


#4 OTHER
set4={1,2,3,4,5,6,7,8}
set5={3,4,5,6}

#4.1 issupperset(), issubset() and isdisjoint()

print(set5.isdisjoint(set4)) # False as these sets have an intersection

print(set5.issubset(set4))#True
print(set4.issuperset(set5))#True

#4.2 copy and clear

new_copy=set5.copy()
print(new_copy) #Copied successfully

set4.clear()
print(set4)  #Cleared


