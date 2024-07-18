yoyo={}#empty dictionary

marks={
    "nirmit":100,
    "issac":55,
    "akash":0,
    0:"harinder",
}

print(marks[0])
print(marks["nirmit"])

# METHOD's 

#1
print(marks.items())
#2

keys={'a','b','c'}
value="NOTHING"

new_dict=dict.fromkeys(keys,value)
print(new_dict)

#3 copy
new_dict=marks.copy()
print(marks)
print(new_dict)

#4 clear
new_dict.clear()
print(new_dict)

#5 get()

print(marks.get("nirmit"))
print(marks.get("yo"))
print(marks.get("yo",4))

#6 update --- You can add or update

marks.update({"nirmit":101, "yadav":99})
print(marks)

#7 keys() and values()

print(marks.keys())
print(marks.values())

#8 pop

marks_2={
    "nirmit":100,
    "issac":55,
    "akash":0,
    0:"harinder",
}

print(marks_2.pop("akash"))
print(marks_2.pop("kaluu",-1))
# print(marks_2.pop("cwcs")) --- throws keyError

#9 popItem
marks_3={
    "nirmit":100,
    "issac":55,
    "akash":0,
    0:"harinder",
}

mar={}

print(marks_3.popitem())
# print(mar.popitem()) --- throws keyError

#10 setdefault(key, default=None): Returns the value of the key if the key is in the dictionary, otherwise inserts key with a value of default and  returns default.

my_dict = {"a": 1}
print(my_dict.setdefault("akash",-10))
print(my_dict.setdefault("aksh",10))
print(my_dict)