dict1={

    "a":1,
    "b":2,
}
dict2={

    "b":3,#This value of b will be merged to new dictiobnary
    "c":2,
}

print(merge:=dict1|dict2) # {'a': 1, 'b': 3, 'c': 2}
